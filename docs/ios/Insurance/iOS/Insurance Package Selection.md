# Insurance Package Selection - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Insurance Package Selection Activity** is the core configuration screen where users compare available insurance plans, customize coverage options (such as duration or vehicle type), review benefits, and initiate the purchase. It acts as the bridge between user profiling and the final checkout.

**Architecture Pattern**: MVVM (Model-View-ViewModel). The `InsurancePackageListViewUI` observes `InsurancePackageListUIViewModel`, which manages the package data state, selection logic, and API interactions.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Navigation**: Accessed from the **Insurance Profile Confirmation Activity** after the user successfully confirms their personal details.
* **Initialization**: Triggers `callWebserviceForFetchingInsuranceList` on appearance to load package configurations.

**User Actions**:
1.  **Select Package**: Tap on a plan card (e.g., "Basic", "Advanced") in the vertical list. The UI updates the selection state visually.
2.  **Customize Coverage**:
    * **Bike Type**: (Bike Insurance Only) Select specific vehicle categories (e.g., "Under 50cc") from a horizontal list.
    * **Duration**: Choose policy term (e.g., "1 Year") via a dropdown menu.
3.  **Review Benefits**:
    * **Primary**: Scroll the "What you get" horizontal carousel.
    * **Secondary**: Review the "Other Benefits" list.
4.  **View Legal**: Tap "View Terms & Conditions" to open the policy document web view.
5.  **Purchase**: Tap the dynamic "Buy at [Price]" button.
    * **Logic**: Triggers the `POST` API to lock the selection, then routes to the next step based on the insurance type.



---

## 3. API Integration

### Endpoint: Get Insurance Packages
**Trigger**: Screen load (`onAppear`).

* **Request Class**: `RequestCreator`
* **Method**: `GET`
* **Endpoint**: `v3/insurance/packages`
* **Parameters**: `categoryId` (String).

**Response Handling**:
* **Success (200)**:
    1.  Parses JSON into `SMBaseInsuranceData`.
    2.  **Auto-Select**: Automatically selects the first package (`packageList[0].isPackageSelected = true`).
    3.  **Bike Logic**: If applicable, parses nested `bikeTypeList` and selects the first option.
* **Failure**: Sets `hasApiFailed`, causing the view to pop back.

### Endpoint: Select Package (Update Order)
**Trigger**: User taps the "Buy at..." button.

* **Request Class**: `RequestCreator`
* **Method**: `POST`
* **Endpoint**: `v3/insurance/package`
* **Body Parameters** (`SMPackageRequest`):
    * `OrderInfo`: Constructed string (e.g., "Purchasing Gym Insurance...").
    * `PackageValue`: Int (Coverage Amount).
    * `InsurancePlanId`: String (Package ID).
    * `InsuranceTermId`: String (Premium Term ID).
    * `Premium`: Int (Cost).
    * `Type`: String (Insurance Type Enum).

**Response Handling**:
* **Success (200)**:
    * Returns `OrderId`.
    * Sets `packageSelectionSuccess = true`, triggering navigation logic in the UI layer.

---

## 4. Data Models & Key Mapping

### 4.1. Insurance Data Model (`SMInsuranceData`)
**File**: `SMBaseInsuranceData.swift`

| JSON Key | Swift Property | UI Component | Purpose of Use |
| :--- | :--- | :--- | :--- |
| `insuranceCoverPage` | `insuranceCoverPage` | **Header Image** | Main visual banner at the top. |
| `packages` | `packageList` | **Main List** | Array of available plans rendered in the package list. |
| `descriptionList` | `descriptionList` | **Other Benefits** | Secondary benefits list. |
| `faqList` | `faqList` | **FAQ** | List of questions and HTML-formatted answers. |

### 4.2. Package Model (`SMInsurancePackage`)
**File**: `SMBaseInsuranceData.swift`

| JSON Key | Swift Property | UI Component | Purpose of Use |
| :--- | :--- | :--- | :--- |
| `packageTitle` | `packageTitle` | **Card Title** | Name of the plan (e.g., "Advanced Package"). |
| `uid` | `uid` / `insurancePlanId` | **Logic** | ID used in the `POST` request to identify the plan. |
| `benefits` | `benefitList` | **Carousel** | Core benefits shown in "What you get". |
| `hasPremiumTermTitle`| `hasPremiumTermTitle`| **Logic** | If true, enables the Bike Type selector logic. |

### 4.3. Premium Term Model (`SMInsurancePremiumTerm`)
**File**: `SMBaseInsuranceData.swift`

| JSON Key | Swift Property | UI Component | Purpose of Use |
| :--- | :--- | :--- | :--- |
| `displayTerm` | `displayTerm` | **Dropdown** | Text for duration selector (e.g., "1 Year"). |
| `finalPremium` | `finalPremium` | **Buy Button** | Price displayed on the sticky bottom button. |
| `uid` | `uid` / `insuranceTermId` | **Logic** | ID used in the `POST` request to identify duration. |

---

## 5. Business Logic

### 5.1. Nested Filtering (Bike Insurance)
The app handles complex pricing structures where the premium depends on both the package *and* a sub-type (e.g., Bike Capacity).
* **Structure**: `SMInsurancePackage` contains `bikeTypeList`, which contains `premiumTermList`.
* **Selection**:
    * User taps a Bike Type -> ViewModel updates `selectedBikeType`.
    * This triggers `updateFilteredPremiumTerm`, which swaps the available options in the Duration Dropdown based on the bike selection.

### 5.2. Purchase Button Dynamic State
* The bottom button's title is a computed property `btnPurchaseTitle`.
* **Standard**: "Buy at [Final Premium]".
* **Discount**: If `discountPercentage > 0`, it renders an attributed string showing the original price (Strikethrough) and the discounted price.

### 5.3. Navigation Routing (Post-Selection)
Upon successful `POST` response (`packageSelectionSuccess`), the app decides the next screen:
1.  **Cardio Insurance**:
    * Checks `isCardioQuestionarieCompleted`.
    * **If False**: Navigates to `CardioInsuranceQuestionsViewUI`.
    * **If True**: Navigates to `ProceedWithEKycPopupViewUI` (Start E-KYC).
2.  **Standard Insurance**:
    * Navigates directly to `InsuranceReviewInfoViewUI`.

---

## 6. Test Cases (Edge & Unit)

### Edge Case 1: API Failure
* **Scenario**: `callWebserviceForFetchingInsuranceList` fails.
* **Result**: `hasApiFailed` becomes true. The UI observes this and immediately pops the view controller to prevent the user from seeing an empty screen.

### Edge Case 2: No Category ID
* **Scenario**: ViewModel initialized without a valid category.
* **Result**: `hasNilCategoryId` is set to true on load. The view pops immediately.

### Edge Case 3: Invalid Selection
* **Scenario**: User attempts to buy without a valid `selectedPremium` (rare, as defaults are set).
* **Result**: `doValidationForUpdatingInsurancePackage` detects nil. Shows toast: "Please select a valid premium term".

### Edge Case 4: E-KYC Required
* **Scenario**: User selects Cardio Insurance.
* **Result**: Instead of the Review screen, the app presents the `CardioInsuranceQuestionsViewUI` or E-KYC popup, ensuring health data is collected before payment.
