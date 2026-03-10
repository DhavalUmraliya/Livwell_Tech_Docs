# Cardio Face Scan Popup - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Cardio Face Scan Popup** (`CardioFaceScanPopupViewUI`) is a retention modal displayed when a user attempts to skip the face scan step in the Cardio Insurance flow. Its primary goal is to incentivize the user to complete the scan by highlighting the "Exclusive Discounts" they will lose if they skip. It serves as a final "Are you sure?" decision gate.

**Architecture Pattern**: Pure SwiftUI View. It is a presentational component that relies on callback closures (`VoidCompletionHandler`) passed during initialization to handle navigation logic.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Invoked from the **Face Scan Info Screen** (`FaceScanInfoForCardioViewUI`) when the user taps the "Skip scan" button in the navigation bar.

**User Actions**:
1.  **Complete Face Scan (Primary)**:
    * **Action**: Tapping the "Complete Face Scan" button.
    * **Outcome**: Dismisses the popup and executes `completeFaceScanCompletion`, which triggers the Face Scan camera flow.
2.  **Skip and Continue (Secondary)**:
    * **Action**: Tapping "Skip and Continue".
    * **Outcome**: Dismisses the popup and executes `skipCompletion`, bypassing the scan and moving directly to the **Review Info** screen (forgoing the discount).
3.  **Cancel (Dismiss)**:
    * **Action**: Tapping the "X" button or the background overlay.
    * **Outcome**: Dismisses the popup without executing any flow completion handlers. The user remains on the **Face Scan Info Screen**.



---

## 3. UI Components & Layout

**Visual Structure**:
* **Overlay**: A semi-transparent dark background (`Color(._201E1F).opacity(0.6)`).
* **Bottom Sheet**: A card anchored to the bottom with a **White Background** (`Color.white`) and top rounded corners (`topCornerRadius(24)`). This differs from the standard dark-themed popups in the app to draw attention.
    * **Illustration**: `lilac_discount_ic` (140x140) centered at the top.
    * **Message Stack**:
        * **Title**: "Want to Unlock Discounts?" (`.manrope(.bold, size: 18)`).
        * **Body**: "Complete your face scan to unlock exclusive discounts." (`.manrope(.regular, size: 14)`).
    * **Buttons**: Uses `AJWhiteVerticalBtnYesNoView`, a variation of the standard button component styled for white backgrounds.

---

## 4. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(...)` | Accepts optional closures for `completeFaceScanCompletion` and `skipCompletion`. |
| `dismissView(completion:)` | Helper function to close the popup and optionally trigger a navigation callback. |
| `AJWhiteVerticalBtnYesNoView` | Custom button component tailored for the light-themed layout of this specific popup. |
