# Cardio Restart Flow Popup - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Cardio Restart Flow Popup** (`CardioRestartWhiteFlowViewUI`) is a retention and confirmation modal designed specifically for the white-themed sections of the Cardio Insurance journey (like the Face Scan Info screen). It interrupts the user when they attempt to exit, reassuring them that their progress is saved and forcing a deliberate choice to stay or leave. Its visual style differs from the standard dark restart popup to match the specific design language of the Cardio flow.

**Architecture Pattern**: Pure SwiftUI View. It relies on `VoidCompletionHandler` closures passed during initialization to handle the navigation logic for "Continue" and "Exit".

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Invoked from the **Face Scan Info View** (`FaceScanInfoForCardioViewUI`) when the user taps the back arrow.

**User Actions**:
1.  **Continue (Stay)**:
    * **Action**: Tapping the "Continue" button.
    * **Outcome**: Dismisses the popup and executes `continueCompletion`. The user remains on the current screen.
2.  **Exit (Leave)**:
    * **Action**: Tapping the "Exit" button.
    * **Outcome**: Dismisses the popup and executes `exitCompletion`. This typically pops the navigation stack back to the Insurance Dashboard.
3.  **Close**:
    * **Action**: Tapping the "X" button.
    * **Outcome**: Same behavior as "Continue" (Dismiss + optional completion).



---

## 3. UI Components & Layout

**Visual Structure**:
* **Overlay**: A semi-transparent dark background (`Color(._201E1F).opacity(0.6)`).
* **Modal Card**: A centered card with a **White Background** (`Color.white`) and rounded corners (`cornerRadius(12)`).
    * **Close Button**: Top-right "xmark" icon (48x48 tap area).
    * **Illustration**: `lilac_discount_ic` (140x140) centered at the top.
    * **Message Stack**:
        * **Title**: "Your progress is saved!" (`.manrope(.bold, size: 18)`, Dark Text).
        * **Body**: "Your details are securely saved! You can resume your purchase anytime..." (`.manrope(.regular, size: 14)`, Gray Text).
    * **Buttons**: Uses `AJWhiteBtnYesNoView`, a custom button component styled for white backgrounds.

---

## 4. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(...)` | Initializes the view with `continueCompletion` and `exitCompletion` closures to handle user decisions. |
| `dismissView(completion:)` | Closes the modal using `navigationCoordinator.dismissPresentedView()` and executes the chosen action. |
| `AJWhiteBtnYesNoView` | A specific variation of the Yes/No button stack designed for light-themed overlays. |
