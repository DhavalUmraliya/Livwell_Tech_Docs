# Coupon Details View - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Coupon Details View Activity** (`CouponDetailsViewUI`) is a simple, informational bottom sheet designed to provide clarity on applied discounts. It displays specific terms, conditions, or explanatory notes related to a coupon that has been successfully applied during the checkout process.

**Architecture Pattern**: Pure SwiftUI View. This screen is purely presentational, displaying data passed to it during initialization.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Tapped from the "Know More" button in the Premium Breakdown section of the **Insurance Checkout Activity** (`GPAInsurancePaymentDetailsView`). This button only appears if `isValidCouponApplied` is true and `couponNotes` are available.

**User Actions**:
1.  **View Details**: Read the detailed message text explaining the coupon's benefits or limitations.
2.  **Dismiss**:
    * **Tap Close Button**: Tapping the "xmark.circle" icon in the top right.
    * **Tap Background**: Tapping the semi-transparent background area.

---

## 3. UI Components & Layout

**Visual Structure**:
* **Overlay**: A semi-transparent black background (`Color(._201E1F).opacity(0.65)`) covers the entire screen.
* **Bottom Sheet**: A content card anchored to the bottom of the screen (`ZStack(alignment: .bottom)`).
    * **Drag Handle**: Standard drag indicator (`SwiftUICommonViews.dragHandler`) at the top.
    * **Title**: "Coupon Details" (`.manrope(.bold, size: 18)`).
    * **Content**: Dynamic `messageText` passed from the parent view model.
    * **Close Button**: An explicit "X" icon in the top-right corner of the sheet.

---

## 4. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(messageText: String)` | Initializes the view with the specific coupon notes string. |
| `dismissView()` | Closes the bottom sheet using `navigationCoordinator.dismissPresentedView()`. |
| `couponDetailsView` | The `ViewBuilder` defining the visual layout of the bottom sheet card. |
