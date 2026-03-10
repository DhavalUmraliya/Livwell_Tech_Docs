# Insurance Congratulation View - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Insurance Congratulation View Activity** (`InsuranceCongratulationViewUI`) acts as the final success state in the insurance purchase journey. Its primary function is to confirm the transaction was successful, inform the user about policy delivery (e.g., "within 24 hours"), and direct them to view their active policies. It effectively closes the purchase loop, preventing backward navigation to the payment screen.

**Architecture Pattern**: Pure SwiftUI View. This screen is presentation-focused and does not rely on a dedicated ViewModel, as the business logic (payment verification) has already concluded in the previous step.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Navigation**: Automatically pushed from the **Insurance Checkout Activity** (`InsuranceCheckoutViewUI`) only after the `successPurchaseComplete` signal is received (i.e., after the backend confirms "PAYMENT_SUCCESS").

**User Actions**:
1.  **View Confirmation**:
    * **Visuals**: Displays a success illustration (`lilac_money_ic`) and a branded background (`lilac_wallet_info_bg_ic`).
    * **Message**: "Successfully Insured" with a subtext explaining that the policy number will be delivered shortly.
2.  **View Policies**:
    * **Trigger**: Tapping the "My Policies" button.
    * **Action**: Navigates to the **My Insurance List View** (`MyInsuranceListViewUI`), passing `isComingPurchase: true` to configure the list view for a post-purchase context (likely managing back-stack behavior).



---

## 3. UI Components & Layout

**Visual Structure**:
* **Background**: Full-screen background image (`lilac_wallet_info_bg_ic`).
* **Illustration**: Centered `lilac_money_ic` image with a 1:1 aspect ratio, padded horizontally.
* **Text Stack**:
    * **Title**: "Successfully Insured" (`.manrope(.bold, size: 18)`).
    * **Subtitle**: "Your insurance is added. Policy number will be delivered within 24 hours." (`.manrope(.regular, size: 14)`, Color `.CFCACC`).
* **Button**: A standard `AJInActiveButtonStyle` button labeled "My Policies" at the bottom.

---

## 4. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `openMyInsuranceListViewUI()` | Initializes `MyInsuranceListViewUI(isComingPurchase: true)` and pushes it to the navigation stack. |
| `swipeGestureEnabled: false` | (Inferred from navigation context) This view is typically pushed with swipe-back disabled to prevent users from returning to the payment processing screen. |
