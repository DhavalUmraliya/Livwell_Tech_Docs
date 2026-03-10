# Insurance Confirm Alert View - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Insurance Confirm Alert View Activity** (`InsuranceConfirmAlertViewUI`) is a mandatory compliance bottom sheet. It requires the user to explicitly agree to the Terms of Use, Disclaimer, and relevant Data Protection policies before the insurance purchase can be finalized. This step creates a binding agreement and unlocks the final "Continue" action to proceed to payment.

**Architecture Pattern**: Pure SwiftUI View. It functions as a modal dialog with internal state management for the checkbox (`isActive`) and callback closures for navigation results.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Invoked from the **Insurance Checkout Activity** (`InsuranceCheckoutViewUI`) when the user taps the final "Buy at [Amount]" button.

**User Actions**:
1.  **Toggle Agreement**: Tap the checkbox (square icon) to agree to the terms.
    * **State Change**: Toggling this updates the `isActive` state. The "Continue" button is only enabled when this is checked (Note: The code defaults `isActive = true` initially, but logic exists to toggle it).
2.  **Read Terms**:
    * **Standard Insurance**: Tap "Terms of Use" or "Disclaimer" links.
    * **Cardio Insurance**: Tap specific embedded links within the Cardio T&C text (e.g., Personal Data Protection, Processing Policy).
    * **Action**: These links open the **Insurance Terms View** (`InsuranceTermsViewUI`).
3.  **Continue**: Tap the "Continue" button.
    * **Logic**: If checked, dismisses the view and executes the `completion` handler with `true`, triggering the payment flow in the parent view. If unchecked, shows a toast message.
4.  **Dismiss**: Tap the transparent background to close the popup without confirming (returns `false` or no action).

---

## 3. UI Components & Layout

**Visual Structure**:
* **Overlay**: A semi-transparent black background (`Color.black.opacity(0.65)`).
* **Bottom Sheet**: A card anchored to the bottom with rounded top corners (`cornerRadius(16, corners: [.topLeft, .topRight])`).
    * **Header**: "Agree to Continue" (`.manrope(.bold, size: 20)`).
    * **Checkbox Row**: A horizontal stack containing the checkmark button and the policy text.
    * **Policy Text**:
        * **Standard**: Two rows of text with underlining for "Terms of Use" and "Disclaimer".
        * **Cardio**: A complex `UIViewRepresentable` label (`CardioInsuranceTCView`) that handles multiple tappable links within a single attributed string.
    * **Button**: "Continue" button using `AJConditionalButtonStyle` to visually indicate enabled/disabled state based on `isActive`.

---

## 4. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(...)` | Accepts `isInsuracnceTypeCardio` and multiple URL strings (Policy, Disclaimer, Data Protection) to configure the view dynamically. |
| `CardioInsuranceTCView` | A `UIViewRepresentable` wrapper for `UILabel` to support tap gesture recognition on specific ranges of an attributed string (e.g., tapping "Personal Data Protection Policy"). |
| `btnContinueClicked()` | Validates `isActive`. If true, calls `dismissView()` and triggers the completion handler. If false, shows a toast. |
| `openInsuranceTermsViewUI` | Navigates to the specific web view for the selected policy document. |
