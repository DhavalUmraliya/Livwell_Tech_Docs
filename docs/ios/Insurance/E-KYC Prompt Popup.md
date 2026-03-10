# E-KYC Prompt Popup - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **E-KYC Prompt Popup** (`ProceedWithEKycPopupViewUI`) is a decision modal that appears before the identity verification phase. It prompts the user to prepare their physical ID card for scanning. Crucially, it offers a "Skip" option, allowing users who may not have their ID handy to proceed with a manual profile verification flow instead, reducing friction and drop-off.

**Architecture Pattern**: Pure SwiftUI View. It operates as a stateless presentation component, delegating navigation logic to closure callbacks passed during initialization.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Invoked from the **Insurance Package Selection** screen (`InsurancePackageListViewUI`) immediately after the user successfully completes the medical questionnaire (`isCardioQuestionarieCompleted == true`) or when the "Contact Me" flow loops back to verification.

**User Actions**:
1.  **Proceed**:
    * **Action**: Tapping the "Proceed" button.
    * **Outcome**: Dismisses the popup and executes `proceedCompletion`. This typically launches the **E-KYC Manager** to start the camera flow.
2.  **Skip for Now**:
    * **Action**: Tapping "Skip for Now".
    * **Outcome**: Dismisses the popup and executes `skipCompletion`. This routes the user to the **Manual Profile Confirmation** screen (`CompleteYourProfilePopupViewUI`).
3.  **Close**:
    * **Action**: Tapping the "X" button in the top right.
    * **Outcome**: Dismisses the popup and executes `dismissCompletion`, usually returning the user to the previous screen.



---

## 3. UI Components & Layout

**Visual Structure**:
* **Overlay**: A semi-transparent dark background (`Color(._201E1F).opacity(0.6)`) covers the screen.
* **Modal Card**: A centered card with a dark background (`Color(._201E1F)` inferred from `blackBg` modifier).
    * **Close Button**: "xmark" icon (36x36) in the top right.
    * **Message Stack**:
        * **Title**: "Ready for e-KYC?" (`.manrope(.bold, size: 18)`).
        * **Body**: "Keep your physical ID ready for quick verification..." (`.manrope(.regular, size: 14)`, Color `.CFCACC`).
    * **Buttons**: Uses `AJVerticalBtnYesNoView` to stack the primary ("Proceed") and secondary ("Skip for Now") actions vertically.

---

## 4. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(...)` | Initializes the view with three distinct callbacks: `proceedCompletion`, `skipCompletion`, and `dismissCompletion` to handle all user choices. |
| `dismissView(completion:)` | A helper method that wraps the standard `navigationCoordinator.dismissPresentedView()` call, ensuring the specific callback is executed only after the animation completes. |
| `AJVerticalBtnYesNoView` | A shared UI component used across the app for consistent vertical button layouts in popups. |
