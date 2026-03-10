# Insurance Checkout - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Insurance Checkout Activity** is the transactional hub of the insurance purchase journey. It provides users with a final breakdown of their selected plan, coverage details, and premium costs. Key functionalities include applying promo codes, reviewing discounts (e.g., from Face Scan), accepting legal terms, and bridging the user to the Payment Gateway for final processing.

**Architecture Pattern**: MVVM (Model-View-ViewModel). The `InsuranceCheckoutViewUI` observes `InsuranceCheckoutUIViewModel`, which manages the complex pricing logic, API orchestration, and asynchronous payment state handling.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Navigation**: Accessed from the **Insurance Review Info Activity** after the user successfully submits their personal details.
* **Initialization**: Triggers `callWebserivceForFetchingInsuranceCheckOutData` on load to retrieve the latest pricing and session data.

**User Actions**:
1.  **Review Summary**: Verify the "Plan Name", "Cover Amount", and "Duration" at the top of the screen.
2.  **Apply Coupon**:
    * Enter a code in the text field and tap "Apply".
    * If valid, the UI updates with the discount amount and a "Remove" option.
    * If invalid, an error message is displayed below the field.
3.  **Review Pricing**: Check the detailed breakdown: Base Premium - Flat Discounts - Face Scan Discount - Promo Discount = **Final Premium**.
4.  **Confirm Purchase**: Tap the sticky bottom button ("Buy at [Amount]").
    * This opens the **Terms & Conditions** bottom sheet (`InsuranceConfirmAlertViewUI`).
    * User must check the "I agree" box and tap "Continue".
5.  **Make Payment**: The app redirects to the Payment Gateway (BaoKim).
    * **Success**: Redirects to `InsuranceCongratulationViewUI`.
    * **Failure/Pending**: Shows an alert popup allowing retry or information status.



---

## 3. API Integration

### Endpoint: Get Checkout Details (Load)
**Trigger**: Screen load (`onAppear`).

* **Request Class**: `RequestCreator`.
* **Method**: `GET`.
* **Endpoint**: `v3/insurance/purchase/checkout`.
* **Parameters**: `categoryId` (String).

**Response Handling**:
* **Success (200)**: Parses JSON into `SMBaseInsuranceCheckout` -> `SMInsuranceCheckoutDetails`. Populates plan details, base premium, and existing discounts (e.g., Face Scan).
* **Failure**: Shows a toast message.

### Endpoint: Apply Coupon
**Trigger**: User taps "Apply" next to the promo code field.

* **Request Class**: `RequestCreator`.
* **Method**: `PUT`.
* **Endpoint**: `.couponDetails` (Inferred).
* **Parameters**: `coupon`, `price`, `insuranceId`, `packageId`.

**Response Handling**:
* **Success**: Updates `baseCoupon` data, recalculates `finalCalculateAmount` locally, and shows discount breakdown.
* **Failure**: Sets `isValidCouponApplied = false` and displays error message.

### Endpoint: Update Checkout (Pre-Payment Lock)
**Trigger**: User taps "Continue" on the T&C Bottom Sheet.

* **Request Class**: `RequestCreator`.
* **Method**: `POST`.
* **Endpoint**: `v3/insurance/purchase/checkout`.
* **Body**: Includes `premium`, `finalPremium`, `flatDiscount` object, and coupon details if applied.

**Response Handling**:
* **Success**: Sets `successInsuranceCheckOutPOST = true`, which triggers the Payment Gateway flow.

### Endpoint: Payment Status Checks
**Trigger**: Callback from Payment SDK (`isBackFromPaymentSDK`).

1.  **Check Status**: `GET v2/payment/complete` with `txnRef`.
    * If `paymentStatus == "PAYMENT_SUCCESS"`, proceed to step 2.
    * If `PAYMENT_PENDING`, show "Payment Processing" alert.
    * Else, show "Payment Failed" alert.
2.  **Complete Purchase**: `PUT v1/insurance/purchase/complete` with `OrderId` and `txnRef`.
    * **Success**: Navigates to **Success Screen**.

---

## 4. Data Models & Key Mapping

### 4.1. Checkout Model (`SMInsuranceCheckoutDetails`)
**File**: `SMBaseInsuranceCheckout.swift`

| JSON Key | Swift Property | UI Component | Purpose of Use |
| :--- | :--- | :--- | :--- |
| `insuranceName` | `insuranceName` | **Header Title** | Screen title (e.g., "Gymer Insurance"). |
| `lastSelectedPlanDetails` | `lastSelectedPlanDetails` | **Plan Card** | Contains `selectedPackage` (Name), `cover` (Value), `selectedTerm` (Duration). |
| `premium` | `premium` | **Breakdown** | The Base Premium amount before discounts. |
| `finalPremiumAfterDiscount` | `finalPremiumAfterDiscount` | **Total** | The final payable amount (used if no coupon is applied). |
| `facescanDiscountPercentageValue` | `formattedFaceScanDiscountAmount` | **Discount Row** | Discount amount derived from E-KYC face scan. |
| `policyContentViewLink` | `policyContentViewLink` | **Legal Link** | URL opened when "Terms of Use" is clicked. |

### 4.2. Coupon Model (`SMInsuranceCoupon`)
**File**: `SMBaseInsuranceData.swift`

| JSON Key | Swift Property | UI Component | Purpose of Use |
| :--- | :--- | :--- | :--- |
| `discountAmount` | `discountAmount` | **Discount Row** | The monetary value deducted by the coupon. |
| `finalAmountAfterDiscount` | `finalAmountAfterDiscount` | **Total** | The recalculated total displayed on the Buy button when a coupon is active. |
| `message` | `message` | **Info Text** | Success/Info message displayed below the pricing section. |

---

## 5. Business Logic

### 5.1. Dynamic Pricing Engine
The `finalCalculateAmount` is computed dynamically based on the state:
* **Scenario A (No Coupon)**: Uses `checkOutData.finalPremiumAfterDiscount` (which already includes FaceScan/Flat discounts calculated by backend).
* **Scenario B (Coupon Applied)**: Uses `baseCoupon.data.finalAmountAfterDiscount` (which applies the coupon on top of existing discounts).
* **Visuals**: The button text updates to show "Buy at [Amount]".

### 5.2. Payment Handshake
The payment flow is a multi-step handshake to ensure data integrity:
1.  **User Agrees**: T&C accepted locally.
2.  **Lock Price**: `POST` to checkout endpoint locks the final price and coupon on the server.
3.  **Initiate Payment**: Payment SDK is launched using the locked order details.
4.  **Verify**: Upon return, the app *must* verify the transaction status with the backend (`v2/payment/complete`) before showing the success screen. Trusting the SDK callback alone is insufficient.

### 5.3. T&C Logic
The `InsuranceConfirmAlertViewUI` adapts based on `isInsuracnceTypeCardio`:
* **Cardio**: Shows specific "Cardio Insurance T&C" links.
* **Standard**: Shows generic "Terms of Use" and "Disclaimer" links.
* **Validation**: The "Continue" button is disabled until the user toggles the checkbox.

---

## 6. Test Cases (Edge & Unit)

### Edge Case 1: Payment Failed
* **Scenario**: User cancels payment or bank rejects it.
* **Result**: `checkPaymentStatusFailure` becomes true. An alert "Payment Failed" appears with a "Re-Try Payment" button (which dismisses the alert).

### Edge Case 2: Payment Pending
* **Scenario**: Bank deduction successful, but backend sync is delayed.
* **Result**: `paymentCompleteFailure` becomes true. An alert "Payment is processing..." appears.

### Edge Case 3: Invalid Coupon
* **Scenario**: User enters an expired code.
* **Result**: API returns error. `isValidCouponApplied` = false. Error message is shown in red under the input field. The total price reverts to the pre-coupon amount.

### Edge Case 4: Already Purchased
* **Scenario**: User navigates to checkout for an owned policy (rare race condition).
* **Result**: The success flow handles duplicates gracefully, or the initial Dashboard check prevents entry. If `successPurchaseComplete` triggers, it routes to `InsuranceCongratulationViewUI` regardless.
