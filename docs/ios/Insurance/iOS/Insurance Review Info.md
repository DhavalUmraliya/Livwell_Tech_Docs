# Insurance Review Info - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Insurance Review Info Activity** serves as the final data collection and verification stage before payment. It presents a summary of the selected insurance plan and the user's personal details. Its primary function is to collect mandatory policy-specific information—such as **National ID**, **Address**, or specific **Bike Details** (Engine/Chassis numbers)—that is required for underwriting but may not exist in the user's base profile.

**Architecture Pattern**: MVVM (Model-View-ViewModel). The `InsuranceReviewInfoViewUI` observes `InsuranceReviewInfoUIViewModel`, which manages data fetching (`v3/insurance/review`), form validation logic, and the submission API call.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Navigation**: Accessed from the **Insurance Package Selection Activity** (after selecting a plan) or the **Cardio E-KYC Flow** (after face scan).
* **Initialization**: Triggers `callWebserviceForFetchingReviewInfo` on load (`onAppear`) using the `categoryId` passed during initialization.

**User Actions**:
1.  **Review Plan**: View high-level plan details. Tapping "View Plan Details" expands the section to show Coverage Amount and Duration.
2.  **Review Profile**: Verify personal information (Name, Gender, DOB, Phone, Email) pre-filled from the user profile or E-KYC data.
3.  **Input Additional Details**:
    * **General Insurance**: Enter "Address" and "National ID".
    * **Bike Insurance**: Enter "Bike Number", "Registration Address", "Chassis Number", and "Engine Number".
4.  **Proceed**: Tap "Proceed to Checkout". This triggers local validation and then posts the data to the backend.
5.  **Back**: Tap the back button to trigger the "Restart Flow" popup (`InsuranceRestartFlowViewUI`).



---

## 3. API Integration

### Endpoint: Get Review Info
**Trigger**: Screen load (`onAppear`), guarded by `!hasApiCalled`.

* **Request Class**: `RequestCreator`
* **Method**: `GET`
* **Endpoint**: `v3/insurance/review`
* **Parameters**: `categoryId` (String).

**Response Handling**:
* **Success (200)**:
    1.  Parses JSON into `SMBaseReviewInfo` -> `SMReviewInfoData`.
    2.  Extracts `requestId` (required for the subsequent POST call).
    3.  Populates the UI with plan details (`lastSelectedPlanDetails`) and user info (`cardioEkycUserInfo` or `UserModel`).
* **Failure**: Shows a toast message with the error description.

### Endpoint: Submit Review Details
**Trigger**: User taps "Proceed to Checkout".

* **Request Class**: `RequestCreator`
* **Method**: `POST`
* **Endpoint**: `v3/insurance/review`
* **Body Parameters**:
    * `requestId`: String (from GET response).
    * `type`: String (Insurance Type).
    * `address`: String (User Input).
    * `nationalId`: String (User Input).
    * **Bike Only**: `engineNumber`, `licenseNumber`, `chassisNumber`, `capacity`.

**Response Handling**:
* **Success (200)**:
    * Sets `successUpdate = true`.
    * Triggers navigation to `InsuranceCheckoutViewUI` via `onReceive` observer.

---

## 4. Data Models & Key Mapping

### 4.1. Review Info Model (`SMReviewInfoData`)
**File**: `SMBaseReviewInfo.swift`

| JSON Key | Swift Property | UI Component | Purpose of Use |
| :--- | :--- | :--- | :--- |
| `insuranceName` | `insuranceName` | **Header Title** | Display title of the screen. |
| `requestId` | `requestId` | **Logic** | ID sent back in the POST request to link the submission. |
| `lastSelectedPlanDetails` | `lastSelectedPlanDetails` | **Plan Card** | Object containing `selectedPackage` (Name), `cover` (Amount), `selectedTerm` (Duration). |
| `cardioEkycUserInfo` | `cardioEkycUserInfo` | **Profile Card** | Used to populate Name, Gender, DOB if `isEkycTaken` is true (Cardio flow). |
| `finalPremiumAfterDiscount` | `discountedPremium` | **Price Label** | The final price displayed in the plan summary. |

### 4.2. Plan Detail Model (`SMLastSelectedPlanDetail`)
**File**: `SMBaseReviewInfo.swift`

| JSON Key | Swift Property | UI Component | Purpose of Use |
| :--- | :--- | :--- | :--- |
| `selectedPackage` | `selectedPackage` | **Text** | Plan Name (e.g., "Silver Plan"). |
| `cover` | `cover` | **Text** | Coverage Amount (e.g., "100,000,000"). |
| `selectedTerm` | `selectedTerm` | **Text** | Duration (e.g., "1 Year"). |

---

## 5. Business Logic

### 5.1. Dynamic Form Rendering
The view conditionally renders input sections based on the `insuranceType` returned by the API:
* **Bike Insurance (`.bikeInsurance`)**: Renders `ReviewBikeInfoView`, requiring Bike Number, Registration Address, Chassis Number, and Engine Number.
* **Other Types**: Renders `ReviewOtherInfoView`, requiring only Address.
* **Always Present**: `ReviewNationalIdView` is always shown for all insurance types.

### 5.2. Input Validation (`doValidationForReviewInfoData`)
Strict validation rules apply before the API call is made:
* **Profile**: Name, Gender, Birthday, Email must be present (checked against `UserModel` or E-KYC data).
* **National ID**: Must be present, exactly 12 characters long, and numeric.
* **Bike Insurance**:
    * Bike Number: Required.
    * Registration Address: Required.
    * Chassis Number: Required, Alphanumeric.
    * Engine Number: Required, Alphanumeric.

### 5.3. Profile Data Source Selection
The ViewModel intelligently selects the source of profile data:
* **Cardio Insurance (Verified)**: If `isEkycTaken` is true, it uses `cardioEkycUserInfo` returned from the API (verified via face scan).
* **Standard Insurance**: It uses `UserModel.main` (local app profile data).

---

## 6. Test Cases (Edge & Unit)

### Edge Case 1: Invalid National ID
* **Scenario**: User enters "123" (too short) or "12345678901A" (alphanumeric).
* **Result**: Validation fails. Toast appears: "Please enter valid National ID" or "Invalid national ID".

### Edge Case 2: Missing Bike Details
* **Scenario**: User selects Bike Insurance but leaves "Chassis Number" empty.
* **Result**: Validation fails. Toast appears: "Please enter Chassis number".

### Edge Case 3: API Update Failure
* **Scenario**: Network error during "Proceed to Checkout" (POST request).
* **Result**: `apiErrorCallBack` triggers. Toast shows error message. Navigation to Checkout does not occur.

### Edge Case 4: E-KYC Data Pre-fill
* **Scenario**: User completes Cardio flow.
* **Result**: `isInsuranceTypeCardio` && `isEkycTaken` are true. Profile fields (Name, DOB) display read-only data from `cardioEkycUserInfo` instead of the generic user profile.
