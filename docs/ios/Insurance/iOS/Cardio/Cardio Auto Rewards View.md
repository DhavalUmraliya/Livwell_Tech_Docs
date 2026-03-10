# Cardio Auto Rewards View - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Cardio Auto Rewards View** (`CardioAutoRewardsViewUI`) is a visually engaging success screen designed to reward users instantly upon unlocking a benefit (likely after a successful purchase or specific milestone in the Cardio flow). It combines celebratory animations (Lottie confetti), audio feedback, and a clear call-to-action to view the unlocked reward.

**Architecture Pattern**: Pure SwiftUI View. It manages its own audio playback state (`AJAudioPlayer`) and relies on internal state for presentation.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Likely invoked from the **Insurance Checkout** or **Success** flow when a specific "Reward Unlocked" condition is met (e.g., `successPurchaseComplete` with a specific reward flag).

**User Actions**:
1.  **Experience Celebration**:
    * **Visual**: A full-screen confetti animation plays once (`loopMode: .playOnce`) over a celebratory background image (`bgOnborading1`).
    * **Audio**: A sound effect (`confitySound.mp3`) plays automatically 0.1s after the view appears.
2.  **View Reward**:
    * **Action**: Tapping the "View Reward" button.
    * **Outcome**: Navigates the user to the specific reward detail or wallet screen (logic to be implemented in the empty action block).
3.  **Close**:
    * **Action**: Tapping the "X" button.
    * **Outcome**: Dismisses the view (logic to be implemented in the empty action block).

---

## 3. UI Components & Layout

**Visual Structure**:
* **Background**: `Color(._201E1F)` (Dark Theme).
* **Animation Layer**: A `ZStack` placing the `LottieView` ("confity") on top of a static background image (`bgOnborading1`), creating a festive atmosphere.
* **Content Card**: A centered modal-like layout:
    * **Close Button**: Top-right "xmark" icon (48x48 tap area).
    * **Greeting**: "Congratulations!" text.
    * **Main Visual**: Large central image `lilac_reward_win_ic` (200x170).
    * **Reward Label**: "Reward Name!" displayed on a dark pill background (`commonBlackBg`).
    * **Message**: "Reward Unlocked" title and "Protection comes with benefits..." subtitle.
    * **Action Button**: "View Reward" (`AJButtonStyle`).

---

## 4. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `AJAudioPlayer` | A helper object responsible for loading and playing the "confitySound.mp3" file. |
| `LottieView` | Integrates the Lottie animation library to render the "confity" JSON animation. |
| `onAppear` | Triggers the sound effect playback with a slight delay to sync with the visual transition. |
