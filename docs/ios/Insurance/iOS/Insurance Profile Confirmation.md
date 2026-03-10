# Insurance Profile Confirmation - Technical Documentation

## 1\. Executive Summary

**Screen Purpose**: The **Insurance Profile Confirmation Activity** functions as a mandatory "Gatekeeper" step in the purchase journey. Its primary role is to validate the user's eligibility (specifically age) and ensure all required personal data (Name, DOB, Gender, Email) is present before allowing access to insurance packages and pricing. This prevents users from purchasing policies they are not eligible for.

**Architecture Pattern**: MVVM (Model-View-ViewModel). The `InsuranceProfileViewUI` observes `InsuranceProfileUIViewModel`, which performs validation logic against the global `UserModel` and the selected `SMInsuranceCategory`.

-----

## 2\. Screen Flow & Navigation

**Entry Point**:

  * **Navigation**: Accessed from the **Insurance Dashboard** (Category Click) or **Landing Page** ("Get Covered" Click).
  * **Context**: Requires an `SMInsuranceCategory` object to be passed during initialization to define age limits and insurance type.

**User Actions**:

1.  **View Header**: See the insurance logo and a "Back" button.
2.  **Check Warnings**: If the user's age is invalid, a warning banner appears at the top: "This insurance package is based on age...".
3.  **Review Details**: Verify personal information (Name, DOB, Phone, Email, Gender).
4.  **Action Buttons**:
      * **Add Details**: If data is missing, this is the only available primary action. Opens the Edit Profile screen.
      * **Confirm**: If data is valid and complete, proceeds to **Insurance Package Selection**.
      * **Update Date of Birth**: Replaces "Confirm" if the age validation fails. Opens Edit Profile.
      * **Edit Details**: Secondary button to modify info even if valid.
5.  **View Benefits**: Static bottom section showing "Instant Coverage", "Flexible Options", etc..

-----

## 3\. API & Data Integration

### Data Sources (Local & Remote)

This screen relies primarily on **Local Data** (`UserModel.main`) validated against **Configuration Data** (`SMInsuranceCategory`).

  * **User Data**: Fetched from the singleton `UserModel.main` (Name, Phone, Email, Gender, DOB).
  * **Insurance Config**: Fetched from the passed `SMInsuranceCategory` object (Age Limits, Logo).

### Analytics Integration

  * **Event**: `insuranceProfileViewed`
      * **Trigger**: `onAppear`
      * **Parameter**: `insuranceType`.
  * **Event**: `insuranceProfileConfirmClicked`
      * **Trigger**: User taps "Confirm"
      * **Parameter**: `insuranceType`.
  * **Event**: `insuranceProfileEditClicked`
      * **Trigger**: User taps "Edit Details"
      * **Parameter**: `insuranceType`.

### Navigation Routing

  * **Confirm Success**:
      * **Action**: Pushes `InsurancePackageListViewUI`.
      * **Logic**: Uses `navigationCoordinator.popToSpecificViewController` logic to manage the stack.
  * **Edit Profile**:
      * **Action**: Calls `AppRouter.openEditProfileViewUI()`.
      * **Refresh**: The ViewModel observes a `refreshToggle` to reload data if the user returns from editing.

-----

## 4\. Data Models & Key Mapping

### 4.1. View Model (`InsuranceProfileUIViewModel`)

**File**: `InsuranceProfileUIViewModel.swift`

| Swift Property | Logic/Source | UI Component | Purpose |
| :--- | :--- | :--- | :--- |
| `logo` | `category?.logo` | **Header Image** | Displays the branding for the selected insurance. |
| `ageMessage` | Dynamic String | **Warning Banner** | Formats the localized error: "Age must be between {min} and {max}". |
| `isUserAgeBetween18To60` | Computed Bool | **Logic Gate** | Determines if the "Confirm" button or "Update DOB" button is shown. |
| `isAddDetails` | Computed Bool | **Logic Gate** | Checks if Gender, DOB, or Email are missing ("NA" or empty). |
| `fullName` | `UserModel.main` | **Row Text** | User's full name. |
| `dob` | `UserModel.main` | **Row Text** | Date of Birth formatted as "dd.MM.yyyy". |
| `phoneNumber` | `UserModel.main` | **Row Text** | Phone number formatted with country code "(+84)". |
| `email` | `UserModel.main` | **Row Text** | Email address. |
| `gender` | `UserModel.main` | **Row Text** | Localized gender string. |

### 4.2. Category Configuration (`SMInsuranceCategory`)

**File**: `SMBaseInsuranceDashboard.swift` (Reference)

| Property | Usage in Profile |
| :--- | :--- |
| `hasAgeLimit` | If `true`, enables the age validation logic. |
| `ageLimit.min` | Lower bound for validation. |
| `ageLimit.max` | Upper bound for validation. |

-----

## 5\. Critical Business Logic Rules

### 5.1. Age Validation Logic

The app strictly enforces age limits before showing prices.

  * **Logic**:
    ```swift
    if category.hasAgeLimit {
       return userDOB.isUserAgeValid(maxAge: category.maxAge, minAge: category.minAge)
    } else {
       return true
    }
    ```
  * **UI Impact**:
      * **Valid**: Warning banner hidden. Button = "Confirm".
      * **Invalid**: Warning banner visible (`ageMessage`). Button = "Update Date of Birth".

### 5.2. Data Completeness Check (`isAddDetails`)

The app ensures no "empty" profiles proceed to underwriting.

  * **Check**: Returns `true` if:
      * `gender` is empty or "NA".
      * `dob` is 0.
      * `email` is empty.
  * **UI Impact**:
      * **True (Missing Data)**: Shows only **one** button: "Add Details".
      * **False (Complete)**: Shows standard "Confirm" and "Edit Details" buttons.

### 5.3. Profile Refresh Mechanism

  * The view contains a `resetId` state variable (`UUID`).
  * When the view appears (`onAppear`), `resetId` is regenerated.
  * The `InsuranceProfileDetailsView` uses `.id(resetId)`, forcing SwiftUI to redraw the component and re-fetch the latest data from `UserModel.main` whenever the view becomes active (e.g., returning from Edit Profile).

-----

## 6\. Test Cases (Edge & Unit)

### Edge Case 1: Underage User

  * **Scenario**: Insurance requires Min Age 18. User is 16.
  * **Result**:
      * `isUserAgeBetween18To60` = `false`.
      * Warning Banner appears: "Age must be between 18 and 60".
      * Primary Button says "Update Date of Birth".
      * Clicking it opens Edit Profile.

### Edge Case 2: Missing Gender

  * **Scenario**: User logged in via phone, hasn't set gender.
  * **Result**:
      * `isAddDetails` = `true`.
      * "Confirm" button is **hidden**.
      * "Add Details" button is visible.
      * Profile row for Gender shows "-".

### Edge Case 3: Successful Confirmation

  * **Scenario**: User data complete and age is valid.
  * **Result**:
      * User clicks "Confirm".
      * Analytics event `insuranceProfileConfirmClicked` is fired.
      * Navigation pushes `InsurancePackageListViewUI`.

### Edge Case 4: No Age Limit

  * **Scenario**: `category.hasAgeLimit` is `false` (e.g., Car Insurance).
  * **Result**:
      * `isUserAgeBetween18To60` returns `true` automatically.
      * Warning banner is never shown.
      * "Confirm" button is available immediately (assuming data is complete).
