# Insurance Landing Page - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Insurance Landing Page Activity** (`InsuranceLandingPagesViewUI`) acts as a high-fidelity digital brochure for specific insurance products (e.g., Cardio Insurance). It is designed to convert users by presenting detailed product information, visual benefit cards, coverage highlights, and customer testimonials in a rich, scrollable layout. It serves as the persuasive entry point before the formal application process begins.

**Architecture Pattern**: MVVM (Model-View-ViewModel). The `InsuranceLandingPagesViewUI` observes `InsuranceLandingPageUIViewModel`, which manages the retrieval of marketing content (`SMInsuranceLandingPage`) and handles navigation state.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Navigation**: Triggered from the **Insurance Dashboard** when a user selects a specific category (e.g., tapping the "Cardio Insurance" card).
* **Deep Link**: Can be launched directly via push notifications. The `onAppear` method checks `AppDelegate.shared.isComingFromDeeplink` to trigger specific analytics (`insuranceLandingPageViewed` with source `pushDeeplink`).

**User Actions**:
1.  **View Hero Content**: See the top banner with the product image, title, and subtitle.
2.  **Browse Benefits**:
    * **Horizontal Scroll**: Swipe through key selling points (icons + text) overlaid on the banner.
    * **Vertical List**: Scroll through detailed benefit cards with tags (e.g., "New", "Popular").
3.  **Read Coverage Info**: View a summary strip regarding coverage details.
4.  **View Testimonials**: Swipe through a carousel of user reviews and ratings.
5.  **Get Covered**: Tap the sticky bottom button ("Get Covered") to initiate the purchase flow.
    * **Action**: This navigates to the **Insurance Profile Confirmation Activity** (`InsuranceProfileViewUI`), passing the current `categoryId` context.

---

## 3. UI Components & Layout

**Visual Structure**:
* **Scroll View**: The main container is a vertical `ScrollView`.
    * **Top Banner**: `InsuranceLandingPagesTopBanerView` displays the hero image and a horizontal list of benefits.
    * **Benefit List**: `InsuranceBenefitListView` (displayed only if `makeContentVisible` is true) renders a vertical stack of detailed cards.
    * **Coverage Strip**: `ListDetailsOfCoverageView` shows a high-level coverage summary.
    * **Testimonials**: `InsuranceTestimonialView` renders a paginated carousel of reviews.
* **Sticky Footer**: A "Get Covered" button fixed at the bottom of the screen, styled with an animated gradient background.

---

## 4. API Integration

### Endpoint: Get Landing Page Data
**Trigger**: Screen load (`onAppear`).

* **Request Class**: `RequestCreator`.
* **Method**: `GET` (Inferred).
* **Endpoint**: `.insuranceLandingPage`.
* **Parameters**:
    * `type`: Insurance Type (e.g., `.cardio`).
    * `categoryId`: String ID.

**Response Handling**:
* **Success (200)**:
    * Parses JSON into `SMInsuranceLandingPage`.
    * Populates `banner`, `cards` (horizontal/vertical), `review`, and `ctaText` data models.
    * Updates `lastSelectedCategory` with age limits and type info for the next screen.
* **Failure**: Sets `hasFailed` to true, which triggers the view to dismiss (pop back).

---

## 5. Data Models & Key Mapping

### 5.1. Landing Page Model (`SMInsuranceLandingPage`)
**File**: `SMInsuranceLandingPage.swift`

| JSON Key | Swift Property | UI Component | Purpose of Use |
| :--- | :--- | :--- | :--- |
| `makeContentVisible` | `makeContentVisible` | **Logic** | Boolean flag controlling the visibility of the vertical benefits list. |
| `banner` | `banner` | **Header** | Contains `image`, `title`, and `subtitle` for the hero section. |
| `cards.horizontal` | `horizontalCardList` | **Carousel** | List of `SMLaningPageHorizontalCard` (Icon, Header, Subtext) shown at the top. |
| `cards.vertical` | `verticalCardList` | **List** | List of `SMLaningPageVerticalCard` (Image, Tag, Header) shown in the body. |
| `review` | `reviewList` | **Reviews** | Array of `SMLaningPageInsuranceReview` containing user rating and text. |
| `ageLimit` | `ageLimit` | **Logic** | Passed to the Profile view to enforce eligibility rules later in the flow. |

---

## 6. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `callWebserviceForFetchingLandingPage()` | Initiates the API request to load all page content. |
| `openProfileView()` | Constructs a temporary `SMInsuranceCategory` using the ViewModel's data and navigates to the **Insurance Profile View**. |
| `InsuranceLandingPagesTopBanerView` | A dedicated sub-view handling the complex layout of the hero image and horizontal benefit cards. |
