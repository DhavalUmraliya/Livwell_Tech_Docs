# Insurance Common Alert View - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Insurance Common Alert View Activity** (`InsuranceCommonAlertViewUI`) is a reusable, data-driven modal dialog designed to communicate critical feedback to the user. It handles various scenarios such as payment failures, processing delays, or purchase confirmations with consistent visual styling and behavior. It ensures users are informed of transaction outcomes and provided with appropriate next steps (e.g., "Re-Try Payment").

**Architecture Pattern**: Pure SwiftUI View. It is configured via an `InsuranceCommonAlertType` enum, which dictates its content (image, text, buttons) and styling, making it highly modular and decoupled from specific business logic.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Displayed by the **Insurance Checkout Activity** (`InsuranceCheckoutViewUI`) in response to payment status updates (e.g., `checkPaymentStatusFailure` or `paymentCompleteFailure`).

**User Actions**:
1.  **View Alert**: Read the status message (e.g., "Payment Failed") and icon.
2.  **Action Button**:
    * **Re-Try**: Tapping "Re-Try Payment" (for failure cases) dismisses the alert, allowing the user to attempt the transaction again.
    * **Ok**: Tapping "Ok" (for success cases) dismisses the alert.
3.  **Dismiss**:
    * **Tap Background**: Tapping the semi-transparent area closes the alert.
    * **Auto-Dismiss**: (Contextual) The parent view typically implements a delay (e.g., 4 seconds) to auto-dismiss informational alerts like "Payment Processing".

---

## 3. UI Components & Layout

**Visual Structure**:
* **Overlay**: A semi-transparent background colored according to the theme (e.g., `Color(._201E1F)` or White) with opacity.
* **Modal Card**: A card anchored to the bottom of the screen (`.frame(maxWidth: .infinity, alignment: .bottom)`).
    * **Drag Handle**: Standard drag indicator at the top.
    * **Illustration**: A centrally configured image (e.g., `lillac_error_ic`) with dynamic sizing (`imgSize`).
    * **Message Stack**:
        * **Title**: Bold header text (e.g., "Purchase Failed").
        * **Body**: Regular text explaining the situation (e.g., "Your purchase didn't go through...").
    * **Button**: A conditional action button (`AJConditionalButtonStyle`) that appears only if `btnTitle` is non-empty.

---

## 4. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(alertType: ...)` | Initializes the view with a specific `InsuranceCommonAlertType` (purchased, paymentFailed, paymentProcessing). |
| `data` (Computed) | Retrieves the `SMInsuranceCommonAlertData` configuration object for the selected alert type. |
| `SMInsuranceCommonAlertData` | A configuration struct defining the title, message, image name, button title, and color theme for each alert state. |
| `dismissView()` | Closes the modal using `navigationCoordinator.dismissPresentedView()` and executes the optional completion closure. |
