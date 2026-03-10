# Cardio Success Purchase View - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Cardio Success Purchase View** (`CardioSuccessPurchaseViewUI`) is a celebratory modal displayed specifically within the Cardio Insurance flow after a user successfully completes the Face Scan verification. Its primary goal is to confirm that the **Face Scan Discount** has been unlocked and applied. It serves as a transition point between the E-KYC/Face Scan process and the final pricing review.

**Architecture Pattern**: MVVM (Model-View-ViewModel). The view observes `CardioSuccessPurchaseUIViewModel`, which formats the success messaging and handles the "Continue" action callback.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Invoked from the **Insurance Package Selection** screen (`InsurancePackageListViewUI`) when the `cardioCompletion` signal is received (indicating successful premium calculation after face scan) AND `isFaceScanDiscountApplied` is true.

**User Actions**:
1.  **View Success Message**:
    * **Header**: "Congratulations [User Name]!".
    * **Visuals**: Confetti/Star background animations (`lilac_stars_square_ic`) and a reward icon (`lilac_reward_win_ic`).
    * **Body**: Text explaining the discount or reward unlocked (e.g., "You've unlocked 15% off").
2.  **Continue**:
    * **Action**: Tapping "Continue to My Coverage".
    * **Outcome**: Dismisses the popup and executes the `completion` closure, which typically navigates the user to the **Insurance Review Info** screen to finalize the purchase with the new price.
3.  **Close**:
    * **Action**: Tapping the "X" button.
    * **Outcome**: Same behavior as "Continue" (Dismiss + Completion Callback).



---

## 3. UI Components & Layout

**Visual Structure**:
* **Overlay**: A semi-transparent dark background (`Color(._201E1F).opacity(0.6)`).
* **Modal Card**: A centered card with a dark background (`Color(._201E1F)` inferred from `blackBg` modifier).
    * **Background Decoration**: `lilac_stars_square_ic` positioned at the top right.
    * **Close Button**: "xmark" icon (36x36) in the top right.
    * **Content Stack**:
        * **User Greeting**: "Congratulations [Name]!" (`.manrope(.semiBold, size: 14)`).
        * **Icon**: Large central reward icon (`lilac_reward_win_ic`, 140x140).
        * **Title**: Dynamic title from API (`faceScanDiscountText.title`).
        * **Message**: Dynamic description from API (`faceScanDiscountText.descriptionField`).
    * **Button**: "Continue to My Coverage" (`AJButtonStyle`) at the bottom.

---

## 4. Business Logic & Data Models

### 4.1. Data Source
The view model is initialized with `SMBaseCardioPremuimTerm`, which contains the results of the face scan processing:
* **User Name**: Extracted from `userDetails.name` to personalize the greeting.
* **Discount Text**: `faceScanDiscountText` object provides the Title and Description displayed on the card, ensuring the messaging matches the specific discount tier achieved.

### 4.2. Navigation Logic
* The view does *not* perform API calls or complex logic itself.
* It relies entirely on the `completion` handler passed during initialization.
* **Flow**: `dismissView()` -> `navigationCoordinator.dismissPresentedView()` -> `viewModel.completion?()`.

---

## 5. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(...)` | Initializes the VM with the premium data and completion closure. |
| `name` (Computed) | Formats the localized string "Congratulations {name}!" by replacing the placeholder with the actual user name. |
| `dismissView()` | Handles the safe dismissal of the modal and triggers the next step in the parent flow. |
