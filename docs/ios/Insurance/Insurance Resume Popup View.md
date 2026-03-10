# Insurance Resume Popup View - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Insurance Resume Popup View** (`InsuranceResumePopupViewUI`) is a decision-gate modal. It intercepts the user flow when they attempt to purchase an insurance product for which they already have an incomplete application. It forces the user to choose between **resuming** their previous session (restoring state) or **restarting** a fresh application (clearing state).

**Architecture Pattern**: MVVM (Model-View-ViewModel). The view observes `InsuranceResumePopupUIViewModel`, which manages the decision logic and performs the necessary API call to reset the journey if "Restart" is chosen.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Invoked from the **Insurance Dashboard** (`InsuranceCategoryView`) when a user selects a category where `resumeInsurancePurchase.canResumeJourney` is true.

**User Actions**:
1.  **Continue (Resume)**:
    * **Action**: Tapping "Continue" dismisses the popup and executes the `proceedCompletion` closure.
    * **Outcome**: The app typically navigates to the saved step using deep linking (`DeepLinkManager`).
2.  **Restart**:
    * **Action**: Tapping "Restart" triggers the `callWebserivceForRestartInsurance()` method in the ViewModel.
    * **Outcome**: If the API call is successful, the popup dismisses, and the `restartCompletion` closure initiates a fresh purchase flow.
3.  **Close/Dismiss**:
    * **Action**: Tapping the "X" button dismisses the popup without taking action.



---

## 3. UI Components & Layout

**Visual Structure**:
* **Overlay**: A semi-transparent black background (`Color(._201E1F).opacity(0.6)`) covers the screen.
* **Modal Card**: A centered card containing:
    * **Close Button**: Top-right "xmark" icon (48x48 tap area).
    * **Text Stack**:
        * **Title**: Dynamic title from the API (e.g., "Continue where you left off?").
        * **Description**: Detailed message explaining the saved state.
    * **Action Buttons**: A vertical layout (`AJVerticalBtnYesNoView`) providing the "Continue" (Yes) and "Restart" (No) options.

---

## 4. Business Logic & Data Models

### 4.1. Data Source
The view is populated using the `SMInsuranceCategory` object passed during initialization. Specifically, it utilizes the nested `resumeInsurancePurchase` object:
* `resumeTitle`: Popup header text.
* `resumeDescription`: Popup body text.
* `categoryId`: Identifier used for the Restart API call.

### 4.2. Restart Logic
When "Restart" is selected:
1.  The ViewModel calls the Restart API (`requestCreator.createRequestForRestertInsurance`).
2.  On **Success (200/201)**: The ViewModel sets `apiCalled = true`.
3.  The View observes `$apiCalled`, dismisses itself, and triggers `restartCompletion`, effectively starting a new journey.

### 4.3. Continue Logic
When "Continue" is selected:
1.  No API call is made by this view.
2.  The View immediately dismisses and triggers `proceedCompletion`.
3.  The parent view (Dashboard) handles the actual deep link navigation based on the saved `resumeScreenDeepLink`.

---

## 5. API Integration

### Endpoint: Restart Insurance Journey
**Trigger**: User taps the "Restart" button.

* **Request Class**: `RequestCreator`.
* **Method**: `PUT` (Inferred from previous API logs).
* **Endpoint**: `v3/insurance/purchase/restart` (Inferred from previous logs).
* **Parameters**:
    * `catID`: The `categoryId` of the insurance product.

**Response Handling**:
* **Success (200/201)**: Logic proceeds to start a new application.
* **Failure**: Shows a toast message with the error description.

---

## 6. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(category: ...)` | Initializes the VM with the category data and completion closures. |
| `callWebserivceForRestartInsurance()` | Performs the network request to clear the saved session on the backend. |
| `dismissView()` | Helper method to close the modal using `navigationCoordinator`. |
| `AJVerticalBtnYesNoView` | Reusable component for the stacked "Continue" vs "Restart" buttons. |
