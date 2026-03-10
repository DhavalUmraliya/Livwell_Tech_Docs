# Cardio Details View - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Cardio Details View** (`CardioDetailsViewUI`) is a specialized product landing screen for Cardio Insurance. It functions as a high-conversion marketing interface, presenting a rich visual layout of benefits ("What You Get") and value propositions ("Why Cardio Insurance"). Crucially, it acts as a **verification gate**, ensuring the user has a verified email address before allowing them to proceed to the purchase flow.

**Architecture Pattern**: MVVM (Model-View-ViewModel). The view observes `CardioDetailsUIViewModel`, which manages the data state (fetched via API) and the email verification status.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Navigation**: Triggered from the **Insurance Dashboard** or **Package Selection** screen when the user selects the "Cardio Insurance" category.

**User Actions**:
1.  **Browse Content**: Scroll vertically to view the hero image, benefit lists, and explanatory carousels.
2.  **Secure Me Now**: Tap the sticky bottom button to initiate the application.
    * **If Email Verified**: The view dismisses (returns `true` to the parent coordinator), allowing the flow to proceed to the Medical Questionnaire.
    * **If Email Unverified**: The app interrupts the flow and presents the **Email Verification Screen** (`EmailFlowViewModel.openEmailScreen`). Upon success, it automatically dismisses the Cardio Details view to proceed.
3.  **Back**: Tap the back arrow (in `CardioPreviewImageView`) to return to the dashboard.



---

## 3. UI Components & Layout

**Visual Structure**:
* **Main Container**: A vertical `ScrollView` with a `LazyVStack` layout.
    * **Header**: `CardioPreviewImageView` displays the top hero image and back button.
    * **Benefits**: `CardioWhatYouGetViewUI` renders a list of key policy features.
    * **Value Prop**: `WhyCardioInsuranceView` renders a horizontal carousel of selling points.
    * **Footer Image**: A final `previewImage` (bottom banner) displayed at the end of the scrollable content.
* **Sticky Button**: The "Secure Me Now" button is pinned to the bottom of the screen (`VStack` layout outside the ScrollView), ensuring it is always accessible.

---

## 4. Business Logic

### 4.1. Email Verification Gate
The view implements a mandatory check for contactability:
* **Trigger**: User taps "Secure Me Now".
* **Check**: `viewModel.isEmailVerified` (Boolean flag from API response).
* **Logic**:
    * **True**: Updates `sharedIsEmailVerified` binding and dismisses the view.
    * **False**: Calls `EmailFlowViewModel.openEmailScreen`. A completion block waits for the email flow to finish successfully before dismissing the Cardio view.

### 4.2. Error Handling
* The view observes `$errorMsg` from the ViewModel.
* If an API error occurs, it dismisses the view and shows a toast message via `CommonFunctions.showToastWithMessage`.

---

## 5. API Integration

### Endpoint: Fetch Cardio Details
**Trigger**: Screen load (`onAppear`).

* **Request**: Calls `viewModel.callWebServiceForFetchingCardioInsuranceDetails()`.
* **API**: `GET` request to `.insuranceCardioContents`.
* **Data**: Populates the images, text content, and the critical `isEmailVerified` status used for the logic gate.

---

## 6. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `btnSecureMeClicked()` | Handles the logic to check `isEmailVerified` and route to either the next step or the Email Verification flow. |
| `CardioPreviewImageView` | A sub-view component responsible for the top navigation bar and hero image. |
| `sharedIsEmailVerified` | A `Binding<Bool>` passed from the parent view model to communicate the verification success state back up the chain. |

---

# E-KYC Manager Service - Technical Documentation

## 1. Executive Summary

**Service Purpose**: The **E-KYC Manager** (`EKYCManager`) is a singleton infrastructure service responsible for handling Identity Verification. It acts as the bridge between the LivWell application, the third-party **FPT.AI E-KYC SDK**, and the LivWell backend. Its primary role is to initialize the biometric capture flow (OCR, Liveness, Face Match), parse the results, and synchronize the session data with the backend for audit and discount eligibility.

**Architecture Pattern**: Singleton Service with Delegation.
* **Access**: `EKYCManager.shared`.
* **Communication**: Utilizes `EKYCManagerDelegate` to report success, failure, or tracking events back to the consuming ViewModel (e.g., `InsurancePackageListUIViewModel`).

---

## 2. Integration Flow

### 2.1. Initialization & Configuration
The manager dynamically configures the FPT.AI SDK based on the current app environment (`serverType`):
* **Dev/Staging**: Uses `eKycKeyDev` and `FEKYCEnvironment.staging`.
* **Prod**: Uses `eKycKeyProd` and `FEKYCEnvironment.product`.

**Configuration Parameters**:
* **Language**: Fetched from `AppUserDefaults` (Dynamic localization).
* **OCR Type**: Fixed to `FEKYCOcrType.idCard` (National ID).
* **Session ID**: Generates a unique `UUID` for every transaction.

### 2.2. The Verification Workflow
**Entry Point**: `doLivWellEKYC(vc: ...)`

1.  **Skip Check**: If `isEkycSkipped` is passed as `true`, the SDK launch is bypassed, and an "empty" log request is sent to the backend to record the user's choice.
2.  **SDK Launch**: If proceeding, `FEKYC.startFPTEKYCFlow` presents the native capture UI on the provided `UIViewController`.
3.  **SDK Callbacks**:
    * **Success**: Returns a raw dictionary containing OCR data, Liveness video URLs, and Face Match scores.
    * **Fail**: Returns an error code/string (e.g., "User Cancelled").
    * **Tracking**: Provides intermediate progress events.



---

## 3. Data Handling & Synchronization

### 3.1. Data Normalization
The FPT SDK returns unstructured dictionary data. The `EKYCManager` parses this immediately into a strongly-typed model `CMEKYCSessionData` using `SwiftyJSON`. This model aggregates:
* **OCR Data**: Extracted Name, ID, DOB.
* **Liveness Data**: Deepfake probability, spoof detection.
* **NFC Data**: Chip data (if applicable).
* **Verify Data**: Matching scores.

### 3.2. Backend Logging (The "Sync" Step)
Crucially, the app does not trust the SDK result in isolation. It performs a mandatory **Server Sync** before unlocking any benefits.

**Endpoint**: `POST v1/insurance/ekyc/liveliness` (Inferred)
* **Request**: Constructed via `RequestCreator.createRequestForUpdateFTP`.
* **Payload**:
    * **Standard**: Full dump of `ocrData`, `liveData`, `nfcData`, `clientUUID`, etc.
    * **Skipped**: Only `insuranceId`, `categoryId`, and `isEkycSkipped: true`.
* **Purpose**: This creates a permanent audit trail of the verification attempt on the LivWell server, which then calculates the `facescanDiscountPercentage` applied in the checkout phase.

---

## 4. Key Methods Reference

| Method | Role |
| :--- | :--- |
| `doLivWellEKYC(...)` | Main entry point. Decides whether to launch SDK or log a "Skip" event. |
| `parseResponseEkyc(...)` | Serializes the raw SDK dictionary into `CMEKYCSessionData` and triggers the backend sync. |
| `callWebserviceForLogger(...)` | Executes the API call to send verification proofs to the backend. |
| `ekycManager(didCompleteWithResult...)` | Delegate method called upon final success/failure to notify the UI layer (e.g., to move to Face Scan). |

---

## 5. Error Handling

* **SDK Errors**: If the FPT SDK fails (e.g., camera permission denied, timeout), the error string is passed to the delegate. Specific errors like "back" (user cancelled) trigger specific UI flows (e.g., showing the "Contact Me" popup).
* **Parsing Errors**: If the SDK returns a result but parsing fails, a "Parsing Failed" error is propagated.
* **Network Errors**: If the backend logging fails, the delegate receives the error. In some debug configurations, mock data (`test_ekyc_json`) might be used for testing.
