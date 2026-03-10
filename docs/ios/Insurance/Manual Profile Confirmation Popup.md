# Manual Profile Confirmation Popup - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Manual Profile Confirmation Popup** (`CompleteYourProfilePopupViewUI`) is a fallback verification screen. It appears when a user chooses to **skip the E-KYC process** during the Cardio Insurance flow. Since the system cannot verify identity via ID card scan, this screen forces the user to manually review their profile data against their legal National ID to ensure accuracy before proceeding.

**Architecture Pattern**: Pure SwiftUI View. It relies on `VoidCompletionHandler` closures passed during initialization to handle navigation logic for "Continue" or "Edit Details".

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Invoked from the **E-KYC Prompt Popup** (`ProceedWithEKycPopupViewUI`) when the user taps "Skip for Now".

**User Actions**:
1.  **Review Data**:
    * **Content**: The user reviews a summary of their profile data: Name, Phone No., Email, Gender, and Date of Birth.
    * **Data Source**: This data is pulled directly from `UserModel.main`, which represents the user's current app profile.
2.  **Continue (Confirm)**:
    * **Action**: Tapping the "Continue" button.
    * **Outcome**: Dismisses the popup and executes `continueCompletion`. This typically advances the user to the **Face Scan Info** screen.
3.  **Edit Details**:
    * **Action**: Tapping "Edit Details".
    * **Outcome**: Dismisses the popup and executes `editProfileCompletion`. This routes the user to the **Edit Profile** screen to correct any discrepancies.
4.  **Close**:
    * **Action**: Tapping the "X" button.
    * **Outcome**: Dismisses the popup via `dismissCompletion` (usually returning to the previous screen).



---

## 3. UI Components & Layout

**Visual Structure**:
* **Overlay**: A semi-transparent dark background (`Color(._201E1F).opacity(0.6)`).
* **Modal Card**: A centered card with a dark background (`blackBg` modifier).
    * **Close Button**: "xmark" icon (36x36) in the top right.
    * **Header Stack**:
        * **Title**: "Confirm Your Profile" (`.manrope(.bold, size: 18)`).
        * **Instruction**: "Please add the following profile details according to your National ID".
    * **Data List**: A vertical stack of `stackView` rows displaying Key-Value pairs (e.g., "Name" - "John Doe").
        * **Formatting**: Handles empty/zero values for Gender and DOB by displaying "-".
    * **Buttons**: Uses `AJVerticalBtnYesNoView` for the "Continue" (Primary) vs "Edit Details" (Secondary) actions.

---

## 4. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(...)` | Initializes the view with three callbacks: `continueCompletion`, `editProfileCompletion`, and `dismissCompletion`. |
| `gender` / `dob` | Computed properties that handle safe unwrapping and formatting of `UserModel` data for display (e.g., converting timestamp to date string). |
| `stackView(title:value:)` | A reusable `ViewBuilder` function that creates consistent label-value rows for the profile data list. |
