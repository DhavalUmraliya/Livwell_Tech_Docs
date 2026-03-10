# Face Scan Info View - Technical Documentation

## 1\. Executive Summary

**Screen Purpose**: The **Face Scan Info View** (`FaceScanInfoForCardioViewUI`) is a mandatory staging screen that precedes the biometric face scan in the Cardio Insurance flow. Its primary technical function is **Data Readiness Verification**. It ensures that the user's profile contains essential biological metrics (Height, Weight, Age, Gender) required for the BMI calculations performed during the scan. It serves as a checkpoint to prevent users from entering the camera flow with incomplete data.

**Architecture Pattern**: MVVM (Model-View-ViewModel). The view observes `FaceScanInfoForCardioUIViewModel`, which performs the validation logic against the global `UserModel` and formats the display data.

-----

## 2\. Screen Flow & Navigation

**Entry Point**:

  * **Trigger**: Invoked from the **Insurance Package Selection** screen (`InsurancePackageListViewUI`) after successful E-KYC or from the **Profile Confirmation Popup** if E-KYC was skipped.

**User Actions**:

1.  **Review Data**: Verify the read-only display of Date of Birth, Gender, Height, and Weight.
2.  **Confirm (Proceed)**:
      * **Condition**: Only available if `isAllRequiredDetailsOkay` is true.
      * **Action**: Tapping "Confirm Details" executes the `cbContinueFScan` closure, launching the camera view for the face scan.
3.  **Update Profile**:
      * **Condition**: Always available. It is the *primary* action if data is missing.
      * **Action**: Tapping "Update Profile Details" opens the **Edit Profile** screen (`AppRouter.openEditProfileViewUI()`).
4.  **Skip**:
      * **Action**: Tapping "Skip scan" in the top-right header.
      * **Outcome**: Opens the **Cardio Face Scan Popup** (`CardioFaceScanPopupViewUI`) to warn the user about losing discounts.
5.  **Exit/Back**:
      * **Action**: Tapping the back arrow.
      * **Outcome**: Opens the **Restart Flow Popup** (`CardioRestartWhiteFlowViewUI`), confirming if the user wants to leave the flow.

-----

## 3\. UI Components & Layout

**Visual Structure**:

  * **Theme**: Unlike most insurance screens, this view uses a **White Background** (`Color.white`) and dark status bar (`.statusBarStyle(.darkContent)`), distinguishing the biometric phase from the dark-themed purchase flow.
  * **Header**: Custom `AJNavigationViewUI` (White Theme) with a "Skip scan" text button on the right.
  * **Content**:
      * **Title**: "Please confirm the following details..." (Multi-line text).
      * **Data Rows**: A vertical stack of `profileInfoView` rows displaying Key-Value pairs (e.g., "Height" - "175 cm").
  * **Bottom Action Area**:
      * **Valid State**: Two stacked buttons – "Confirm Details" (`AJButtonStyle`) and "Update Profile Details" (Outlined Style).
      * **Invalid State**: Single button – "Update Profile Details" (`AJButtonStyle`).

-----

## 4\. Business Logic & Data Models

### 4.1. Data Validation (`checkAllRequiredDetails`)

The ViewModel enforces strict data completeness rules necessary for the health assessment algorithms:

  * **Logic**:
    ```swift
    private func checkforBMIData() -> Bool {
        // Returns true only if Email, Height, Weight, DOB, and Gender are non-empty/non-zero
    }
    ```
  * **Impact**: Sets `isAllRequiredDetailsOkay`. If `false`, the user is **blocked** from proceeding to the scan and must update their profile.

### 4.2. Data Formatting

The ViewModel handles unit conversion and display formatting for the UI:

  * **Height**: Formats based on `UserModel.main.heightUnit` (Cms, Inch, Mts). Example: "175 cm" or "5 ft'in".
  * **Weight**: Formats based on `UserModel.main.weightUnit` (Kgs, Lbs).
  * **Date**: Converts timestamp to "dd/MM/yyyy" format.

-----

## 5\. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(...)` | Initializes with a `VoidCompletionHandler` (`cbContinueFScan`) used to signal the parent coordinator to launch the camera. |
| `btnViews` | A computed view that conditionally renders the button stack based on the validation state. |
| `opCardioRestartWhiteFlowView` | Presents the white-themed restart popup, specific to this screen's design language. |
| `openCardioFaceScanPopupView` | Presents the discount retention popup when skipping. |
