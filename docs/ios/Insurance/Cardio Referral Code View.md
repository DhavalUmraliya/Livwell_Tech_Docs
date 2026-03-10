# Cardio Referral Code View - Technical Documentation

## 1\. Executive Summary

**Screen Purpose**: The **Cardio Referral Code View** (`CardioReferralCodeViewUI`) is a dedicated bottom sheet for inputting and validating referral codes during the Cardio Insurance purchase flow. It allows users to apply a code that might link their policy to a specific agent or campaign. It features real-time local validation and communicates the result back to the parent checkout screen for API verification.

**Architecture Pattern**: MVVM (Model-View-ViewModel). The view observes `CardioReferralCodeUIViewModel`, which handles the input state, validation logic, and completion callbacks.

-----

## 2\. Screen Flow & Navigation

**Entry Point**:

  * **Trigger**: Invoked from the **Insurance Checkout Activity** (`GPAInsurancePaymentDetailsView`) when the user taps the "Have a referral code?" link.

**User Actions**:

1.  **Enter Code**: Type a referral code into the input field.
      * **Feedback**: A checkmark icon appears if the field is not empty (visually managed by the input component).
2.  **Validation (Real-time)**:
      * As the user types, the ViewModel checks the length.
      * If the code is too short (≤ 2 characters), `isCodeEmpty` becomes true, potentially showing an error message if the user tries to submit.
3.  **Apply**: Tap the "Apply" button.
      * **Action**: Triggers `viewModel.validateCode()`.
      * **Success**: If valid, the view dismisses, and the code is passed back via the `completion` handler.
      * **Failure**: If invalid, a toast message ("Please enter a valid referral code") is shown.
4.  **Dismiss**: Tap the background overlay to close the modal without applying a code.

-----

## 3\. UI Components & Layout

**Visual Structure**:

  * **Overlay**: A semi-transparent dark background (`Color(._201E1F).opacity(0.6)`).
  * **Bottom Sheet**: A card anchored to the bottom with rounded top corners (`topCornerRadius(24)`).
      * **Drag Handle**: Standard indicator (`SwiftUICommonViews.dragHandler`).
      * **Title**: "Enter referral code" (`.manrope(.semiBold, size: 18)`).
      * **Input Field**: A text input field with a placeholder. Displays a green checkmark icon when active.
      * **Error Text**: "Invalid Code" displayed in red (`Color(.F03457)`) if `isCodeEmpty` is true.
      * **Button**: "Apply" button (`AJConditionalButtonStyle`) that enables/disables based on input validity.

-----

## 4\. Business Logic & Data Models

### 4.1. Validation Logic (`CardioReferralCodeUIViewModel`)

The ViewModel enforces local validation rules before passing the code to the backend:

  * **Rule**: Code length must be greater than 2 characters.
  * **Logic**:
    ```swift
    func validateCode() {
        if referralCode.count <= 2 {
            // Show Toast, set isCodeEmpty = true
        } else {
            // Success: Dismiss and callback
        }
    }
    ```
  * **Reactive Update**: The View uses `.onChange(of: viewModel.referralCode)` to update the `isCodeEmpty` flag in real-time as the user types, which toggles the button state.

### 4.2. Callback Handling

  * The view is initialized with a `StringCompletionHandler`.
  * Upon successful validation, this handler transmits the `referralCode` string back to the **Insurance Checkout ViewModel**, which then performs the actual API call (`createRequestForApplyReferralCode`).

-----

## 5\. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(completion: ...)` | Initializes the VM with a closure to return the entered code upon success. |
| `validateCode()` | Performs final validation check on button tap and triggers the dismissal/callback. |
| `isCodeEmpty` | A published boolean state that controls the visibility of the error message and the active state of the "Apply" button. |
