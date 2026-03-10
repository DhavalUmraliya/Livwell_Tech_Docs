# Cardio Contact Me Popup - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Cardio Contact Me Popup** (`CardioContactMePopUpViewUI`) is a retention and assistance modal designed to capture users who are hesitating or encountering issues during the Cardio Insurance application (e.g., after an E-KYC cancellation). It offers a direct line to sales support ("I'm Interested") or allows the user to exit the flow ("Later"). Its goal is to prevent drop-off by offering personalized guidance.

**Architecture Pattern**: Pure SwiftUI View. It is a presentational component that relies on callback closures (`VoidCompletionHandler`) passed during initialization to handle the navigation logic for the "Interested" and "Later" actions.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Invoked from the **Insurance Package Selection** screen (`InsurancePackageListViewUI`) specifically when the E-KYC process returns a "back" error (indicating user cancellation) or potentially when a user attempts to exit a critical step.

**User Actions**:
1.  **I'm Interested (Primary)**:
    * **Action**: Tapping the "I'm Interested" button.
    * **Outcome**: Dismisses the popup and executes `continueCompletion`.
    * **Business Logic**: Typically routes the user to a flow where they can request a callback or re-attempt the verification process (e.g., retrying E-KYC).
2.  **Later (Secondary)**:
    * **Action**: Tapping "Later".
    * **Outcome**: Dismisses the popup and executes `skipCompletion`, usually navigating the user back to the previous screen or dashboard.



---

## 3. UI Components & Layout

**Visual Structure**:
* **Overlay**: A semi-transparent dark background (`Color(._201E1F).opacity(0.6)`).
* **Bottom Sheet**: A card anchored to the bottom of the screen (`.frame(maxWidth: .infinity, alignment: .bottom)`).
    * **Styling**: Dark background (`Color(._201E1F)`) with top rounded corners (`topCornerRadius(24)`).
    * **Illustration**: `lilac_contact_me_consent_ic` (140x140) centered at the top.
    * **Message Stack**:
        * **Title**: "Need Help Deciding?" (`.manrope(.bold, size: 18)`).
        * **Body**: "We’d love to guide you on your heart health and protection journey." (`.manrope(.regular, size: 14)`).
    * **Buttons**: Uses `AJVerticalBtnYesNoView` for the stacked decision buttons ("I'm Interested" vs "Later").

---

## 4. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(...)` | Accepts optional closures for `continueCompletion` and `skipCompletion` to handle user choices. |
| `dismissView(completion:)` | Helper function to close the bottom sheet and execute the selected action callback. |
| `AJVerticalBtnYesNoView` | Reusable component for the vertical button layout, consistent with other dark-themed popups in the app. |
