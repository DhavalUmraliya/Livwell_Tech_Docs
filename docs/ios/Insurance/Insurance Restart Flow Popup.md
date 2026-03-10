# Insurance Restart Flow Popup - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Insurance Restart Flow Popup** (`InsuranceRestartFlowViewUI`) is a modal confirmation dialog. It appears when a user attempts to exit the insurance purchase journey (e.g., by tapping "Back" on the Review or Checkout screens) before completion. Its primary goal is to prevent accidental drop-offs by reassuring the user that their progress has been saved and offering a clear choice to stay or exit.

**Architecture Pattern**: Pure SwiftUI View. It does not have a dedicated ViewModel but interacts directly with the `navigationCoordinator` to manage stack navigation.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Invoked when the user taps the "Back" button on the **Insurance Review Info Activity** or **Insurance Checkout Activity**.

**User Actions**:
1.  **Continue (Stay)**: Tapping "Continue" dismisses the popup, keeping the user on the current screen so they can proceed with the purchase.
2.  **Exit (Leave)**: Tapping "Exit" confirms the departure.
    * **Action**: The app navigates back to the **Insurance Dashboard** (Root).
    * **State Update**: It triggers a refresh on the Dashboard (`callWebServiceForFetchingInsuranceCategoryList`) to ensure the "Resume Journey" card is correctly displayed when the user returns.



---

## 3. UI Components & Layout

**Visual Structure**:
* **Overlay**: A semi-transparent black background (`Color(._201E1F).opacity(0.65)`) covers the screen.
* **Card**: A centered content card containing:
    * **Icon**: `lilac_contact_me_consent_ic` (140x140).
    * **Title**: "Your progress is saved!" (`InsurancePurchaseFlowStrings.yourProgressIsSaved`).
    * **Description**: "Your details are securely saved! You can resume your purchase anytime from where you left off.".
    * **Buttons**: A vertical "Yes/No" button set (`AJBtnYesNoView`).

---

## 4. Business Logic & Navigation

### 4.1. Dashboard Refresh Logic (`MapsToRoot`)
When the user chooses to **Exit**, the view performs a specific cleanup sequence to ensure the app state is consistent:
1.  **Dismiss**: Closes the popup itself.
2.  **Locate Dashboard**: Checks if `FinanceContainerViewUI` exists in the navigation stack.
3.  **Refresh Data**: Accesses `FinanceContainerUIViewModel` and calls `callWebServiceForFetchingInsuranceCategoryList()`. This is critical because the backend now holds a "Saved State" for this purchase, and the Dashboard needs to fetch this new state to show the "Resume" popup next time.
4.  **Pop**: Calls `navigationCoordinator.popToSpecificViewController(atIndex: 1)` to return to the Insurance Dashboard.

---

## 5. Key Code Reference

| Method | Purpose |
| :--- | :--- |
| `dismissView()` | Closes the popup using `navigationCoordinator.dismissPresentedView()`. |
| `MapsToRoot()` | Handles the logic to refresh the dashboard API and pop the navigation stack back to the root insurance screen. |
| `progressSavedView` | The SwiftUI `ViewBuilder` property defining the visual layout of the confirmation card. |
