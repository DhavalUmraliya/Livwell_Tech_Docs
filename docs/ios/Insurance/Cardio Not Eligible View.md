# Cardio Not Eligible View - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Cardio Not Eligible View** (`CardioNotEligibleViewUI`) is a "Hard Stop" modal displayed when a user fails the medical underwriting questionnaire for Cardio Insurance. Rather than simply blocking the user, it functions as a **Cross-Sell / Retention** screen. It explains why the user is ineligible and immediately suggests an alternative insurance plan (e.g., Gym Insurance) that better fits their profile, attempting to keep the user within the sales funnel.

**Architecture Pattern**: MVVM (Model-View-ViewModel). The view observes `CardioNotEligibleUIViewModel`, which processes the eligibility response data (`SMBaseCardioEligiblityStatus`) passed from the previous screen.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Invoked from the **Insurance Package Selection** screen (`InsurancePackageListViewUI`) when the `checkQuestionCerteria` API returns `isCardioInsuranceEligible == false`.

**User Actions**:
1.  **View Rejection Message**:
    * **Visuals**: A warning icon (`Lilac_CircleWavyWarning`) at the top indicating the stop state.
    * **Message**: A dynamic title and description explaining the ineligibility reason.
2.  **View Alternative Plan**:
    * **Card**: A highlighted card showing a recommended alternative (e.g., "Gym Insurance") with a list of its specific benefits.
    * **Explore**: Tapping "Explore all" or the main "View all Insurances" button.
3.  **Navigation**:
    * **Specific Plan**: Tapping "View all Insurances" typically triggers a deep link to the suggested product.
    * **Exit**: Tapping "Explore all" or the background dismisses the view and routes the user back to a safe landing spot (Dashboard, Home, etc.) depending on where they entered the flow.



---

## 3. UI Components & Layout

**Visual Structure**:
* **Overlay**: A semi-transparent background covering the screen.
* **Modal Card**: A full-screen-height modal anchored to the bottom.
    * **Header**: Warning icon and explanatory text.
    * **Cross-Sell Section**:
        * **Header**: "Plan Text" (e.g., "You might like") and "Explore all" button.
        * **Product Card**: A styled container (`blackBg`, `roundedBorder`) displaying:
            * **Title**: Insurance Type (e.g., "Gym Insurance").
            * **Benefits**: A vertical list of `SMBenefit` items (Icon + Text).
            * **Image**: Large product illustration on the right.
    * **Primary Button**: "View all Insurances" (`AJButtonStyle`) pinned to the bottom content area.

---

## 4. Business Logic & Data Models

### 4.1. Data Source (`SMIneligibleData`)
The view is entirely data-driven by the `SMIneligibleData` object contained within the API response:
* `title` / `description_`: Explains the rejection.
* `insuranceType`: The name of the alternative plan.
* `benefits`: Array of `SMBenefit` used to populate the cross-sell card.
* `bannerLink`: Deep link URL used to navigate to the alternative plan.

### 4.2. Context-Aware Navigation
The `btnExploreAllClicked` function handles complex routing based on the `comingFrom` enum passed during initialization. This ensures the user is returned to the correct context:
* **.insurance**: Resets the category list and pops to the Insurance Dashboard (Index 1).
* **.home**: Pops to the Home Tab (Index 0).
* **.cfyc**: Pops to the CFYC container.
* **.faceScan**: Pops to the root.

### 4.3. Deep Linking
The "View all Insurances" button uses `DeepLinkManager` to execute the `bannerLink` provided by the backend. This allows the server to dynamically determine *which* specific insurance product to redirect the ineligible user to.

---

## 5. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(...)` | Initializes the VM with the eligibility status data and the `comingFrom` source context. |
| `btnExploreAllClicked()` | Handles the logic for "Exit" navigation, ensuring the stack is popped to the correct root controller based on user origin. |
| `btnExploreInsuranceClicked()` | Executes the deep link associated with the alternative insurance plan. |
| `SMIneligibleData` | The model struct containing the cross-sell marketing data (Benefits, Images, Links). |
