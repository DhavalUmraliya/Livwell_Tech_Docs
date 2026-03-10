# Insurance Dashboard - Technical Documentation

## 1\. Executive Summary

**Screen Purpose**: The **Insurance Dashboard Activity** (implemented as `FinanceContainerViewUI`) acts as the central hub for the user's insurance interactions. It aggregates the user's LWC (LivWell Coin) balance, active policy status, available insurance products, promotional banners, testimonials, and support options into a single scrollable view.

**Architecture Pattern**: MVVM (Model-View-ViewModel). The `FinanceContainerViewUI` observes `FinanceContainerUIViewModel`, which manages state, API calls, and business logic.

-----

## 2\. Screen Flow & Navigation

**Entry Point**:

  * **Navigation**: Accessed via the main dashboard or tab bar, typically represented as the "Insurance" or "Finance" section.
  * **Initialization**: The screen triggers an API call (`callWebServiceForFetchingInsuranceCategoryList`) on first appearance (`onAppear`) to fetch the insurance dashboard data.

**User Actions**:

1.  **Check Balance**: View real-time LWC balance in the top-right header.
2.  **View Policies**: If policies exist, the "My Policies" card (`PurchasedPolicyView`) is shown. Tapping it opens `MyInsuranceListViewUI`.
3.  **Browse Insurance**:
      * **Internal Products**: Tap a category (e.g., "Personal Accident") to start a purchase flow (`InsuranceProfileViewUI`).
      * **External Products**: Tap a category (e.g., "Car Insurance") to open a lead generation web view (`LeadGenrationWebViewController`).
      * **Resume Journey**: If a purchase was interrupted, a resume popup appears (`InsuranceResumePopupViewUI`) allowing the user to continue or restart.
4.  **View Promotions**: Scroll horizontally through banners. Tapping a banner triggers deep links or external URLs.
5.  **Get Support**: Tap buttons in the `GetAssistanceView` to call customer care or open Facebook support.

-----

## 3\. API Integration

### Endpoint: Get Insurance Dashboard

**Trigger**: Screen load (`onAppear`), guarded by `!hasApiCalled`.

  * **Request Class**: `RequestCreator`
  * **Method**: `GET`
  * **Endpoint**: `v4/insurance`
  * **Parameters**: None (session-based).

**Response Handling**:

  * **Success (200)**:
    1.  Parses JSON into `SMBaseInsuranceDashboard`.
    2.  Populates `categoryList`, `historyList`, `bannerList`, and `testimonialList`.
    3.  Sets the first category as selected by default.
  * **Failure**: Shows a toast message with the error description.

-----

## 4\. Response Model Structure

The following JSON model represents the structure returned by `v4/insurance`.

```json
{
  "message": "INSURANCE_SCHEDULE",
  "type": "INSURANCE_SCHEDULE",
  "statusCode": 200,
  "data": {
    "historyList": [], 
    "categorylist": [
      {
        "_id": "67cfec3d1ab17f3710aac75c",
        "name": "Gymer Insurance",
        "type": "GYM_PERSONAL_ACCIDENT_INSURANCE",
        "resourceType": "INTERNAL",
        "image": "https://...",
        "logo": "https://...",
        "price": 367000,
        "packageValueAmount": 205000000,
        "hasAgeLimit": true,
        "ageLimit": { "min": 18, "max": 60 },
        "resumeInsurancePurchase": {
          "canResumeJourney": false
        }
      },
      {
        "_id": "67cffb201ab17f3710aac803",
        "name": "Car Insurance",
        "type": "CAR_INSURANCE",
        "resourceType": "EXTERNAL",
        "url": "https://sunlife.livwell.asia/...",
        "image": "https://...",
        "hasAgeLimit": false
      }
    ],
    "banners": [
      {
        "_id": "68677da1375330605f4d90cb",
        "type": "INSURANCE_REFFERAL",
        "linkType": "INTERNAL",
        "bannerLink": "open://livwell/insuranceCommonLandingPage?categoryId=...",
        "image": "https://...",
        "title": "Redirect Bike Banner"
      }
    ],
    "testimonialList": [
      {
        "name": "Linh",
        "testimonial": "A variety of insurance packages...",
        "image": "https://..."
      }
    ],
    "resumeInsurancePurchase": {
      "canResumeJourney": false,
      "resumeScreenDeepLink": ""
    }
  }
}
```

-----

## 5\. Data Models & Key Mapping

### 5.1. Insurance Category Model (`SMInsuranceCategory`)

**File**: `SMBaseInsuranceDashboard.swift`

| JSON Key | Swift Property | UI Component | Purpose of Use |
| :--- | :--- | :--- | :--- |
| `name` | `name` | **Grid Item Text** | Display name of the insurance product (e.g., "Gymer Insurance"). |
| `image` | `image` | **Grid Item Image** | Icon/Thumbnail for the insurance category. |
| `resourceType` | `resourceType` | **Logic** | Determines click behavior: `INTERNAL` opens native flow, `EXTERNAL` opens web view. |
| `url` | `url` | **Logic** | URL used for `EXTERNAL` resource types (Lead Gen WebView). |
| `resumeInsurancePurchase` | `resumeInsurancePurchase` | **Logic** | Object containing `canResumeJourney`. If true, shows the "Resume/Restart" popup. |
| `type` | `insuranceType` | **Logic** | Enum (e.g., `.cardio`) used to route to specific screens like `CardioDetailsViewUI` vs generic `InsuranceProfileViewUI`. |

### 5.2. Banner Model (`SMBanners`)

**File**: `SMBaseInsuranceDashboard.swift`

| JSON Key | Swift Property | UI Component | Purpose of Use |
| :--- | :--- | :--- | :--- |
| `image` | `image` | **Banner Card** | Visual image for the promotional banner. |
| `linkType` | `eLinkType` | **Logic** | Determines navigation: `INTERNAL` uses DeepLinkManager, `EXTERNAL` uses Safari. |
| `bannerLink` | `bannerLink` | **Action** | The URL or deep link string executed on tap. |
| `title` | `title` | **Analytics** | Used for tracking banner clicks in MoEngage. |

### 5.3. History/Policy Model (`SMInsuranceHistory`)

**File**: `SMBaseInsuranceDashboard.swift`

| JSON Key | Swift Property | UI Component | Purpose of Use |
| :--- | :--- | :--- | :--- |
| `historyList` | `historyList` | **Visibility** | If this array is not empty, the "Purchased Policy" view is displayed. |
| `policy` | `formattedPolicy` | **UI (Potential)** | Although not shown on the dashboard summary card, this data populates the list view when "My Policies" is tapped. |

### 5.4. Testimonial Model (`SMTestimonialList`)

**File**: `SMBaseInsuranceDashboard.swift`

| JSON Key | Swift Property | UI Component | Purpose of Use |
| :--- | :--- | :--- | :--- |
| `testimonial` | `testimonial` | **Card Text** | The quote text from the user. |
| `name` | `name` | **Card Footer** | Name of the person giving the testimonial. |
| `image` | `image` | **Card Avatar** | Avatar image of the user. |

-----

## 6\. Business Logic

### 6.1. Dynamic Section Visibility

The dashboard uses conditional rendering (`if viewModel.is...Available`) to hide empty sections:

  * **My Policies**: Hidden if `historyList` is empty.
  * **Categories**: Hidden if `categoryList` is empty.
  * **Banners**: Hidden if `bannerList` is empty.
  * **Testimonials**: Hidden if `testimonialList` is empty.

### 6.2. Insurance Purchase Routing

When an insurance category is selected, the app evaluates:

1.  **Resource Type**:
      * `EXTERNAL`: Opens `LeadGenrationWebViewController` with the provided `url`.
      * `INTERNAL`: Proceed to step 2.
2.  **Resume Capability**:
      * Checks `category.resumeInsurancePurchase.canResumeJourney`.
      * **True**: Shows `InsuranceResumePopupViewUI`. User can "Continue" (DeepLink) or "Start New" (Reset flow).
      * **False**: Proceed to step 3.
3.  **Insurance Type**:
      * `CARDIO`: Routes to `CardioDetailsViewUI` (requires email verification).
      * **Other**: Routes to standard `InsuranceProfileViewUI`.

### 6.3. Deep Linking

Banners and Resume actions utilize `DeepLinkManager`. If an internal deep link fails to resolve (`isOpened == false`), the app falls back to opening the link in Safari.

-----

## 7\. Test Cases (Edge & Unit)

### Edge Case 1: No Insurance History

  * **Scenario**: New user with no purchases.
  * **Result**: API returns empty `historyList`. `viewModel.isHistoryPolicyAvailable` is `false`. The `PurchasedPolicyView` is hidden.

### Edge Case 2: External Insurance Link

  * **Scenario**: User taps "Car Insurance".
  * **Result**: `resourceType` is `EXTERNAL`. App navigates to `LeadGenrationWebViewController` loading the `url` from the API response.

### Edge Case 3: Resume Journey

  * **Scenario**: User taps an insurance they previously started but didn't finish.
  * **Result**: `canResumeJourney` is `true`. A popup appears. Tapping "Resume" triggers the deep link found in `resumeInsurancePurchase`.

### Edge Case 4: API Failure

  * **Scenario**: Network timeout.
  * **Result**: `apiErrorCallBack` hides the loader. A toast message displays the error. The screen remains on the previous state or empty.

### Edge Case 5: Empty Banner List

  * **Scenario**: No active promotions.
  * **Result**: `bannerList` is empty. `InsuranceBannerView` is not added to the view hierarchy.
