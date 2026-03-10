# Insurance Already Purchased View - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Insurance Already Purchased View Activity** (`InsuranceAlreadyPurchasedViewUI`) is a feedback modal designed to handle the scenario where a user attempts to purchase an insurance policy they already hold (or, alternatively, if the insurance is unavailable). It prevents duplicate purchases and redirects the user to view their existing coverage.

**Architecture Pattern**: Pure SwiftUI View. It operates as a simple presentation layer, determining its message and button behavior based on a single boolean state passed during initialization.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Invoked from the **Insurance Package Selection Activity** (`InsurancePackageListViewUI`) when the user taps "Buy" if the ViewModel's `isPurchased` flag is true.

**User Actions**:
1.  **View Message**:
    * **Purchased State**: "You’ve already purchased insurance! Check your details anytime under 'My Policies'".
    * **Unavailable State**: "Sorry, this insurance is not available for purchase please come back later.".
2.  **Dismiss**:
    * **Tap Button**: Tapping "Ok" (if purchased) or "Continue" (if unavailable) dismisses the popup.
    * **Tap Background**: Tapping the transparent area outside the card also dismisses the view.

---

## 3. UI Components & Layout

**Visual Structure**:
* **Overlay**: A semi-transparent background (`Color(._201E1F).opacity(0.65)`).
* **Bottom Sheet**: A card anchored to the bottom of the screen (`.frame(maxWidth: .infinity, alignment: .bottom)`).
    * **Illustration**: A "Search" icon (`lilac_search_ic`) sized 140x140.
    * **Message**: Text describing the status, styled with `.manrope(.regular, size: 14)` and a specific gray color (`Color.CFCACC`).
    * **Button**: A primary action button (`AJButtonStyle`) to acknowledge the message.

---

## 4. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(isPurchaseAvailable: Bool)` | Initializes the view. Defaults to `true` (Purchased state). If `false`, it shows the "Unavailable" message. |
| `msg` (Computed Property) | Dynamically returns the correct localized string based on `isPurchaseAvailable`. |
| `dismissView()` | Closes the modal using `navigationCoordinator.dismissPresentedView()`. |
