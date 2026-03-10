# Screen: Prize Reveal

The **Prize Reveal** screen is the rewarding climax of the Monopoly experience. It can display an instant reward, a collected sticker (for the grand prize puzzle), or a "Better Luck Next Time" message.

## Metadata
- **View File**: `MonopolyGrandPriceDisplayView.swift`
- **ViewModel File**: `MonopolyGrandPriceDisplayViewModel.swift`
- **Feature Name**: Prize Reveal

## Key Components

### 1. Interactive Gift Box
- Initially shows a closed, "jiggling" gift box (`bt_grand_prize_icon`).
- Users must tap to trigger the "Open" animation.
- Uses a `JelloEffect` view modifier for a playful, bouncy physical feel.

### 2. Reward Display
- **Grand Prize Sticker**: Shows the specific sticker image.
- **Instant Gift**: Displays the reward card (voucher, points, etc.).
- **Better Luck Next Time**: Shows a simplified card for non-winning rolls.

### 3. Visual Effects
- **Confetti**: A Lottie animation (`confity_lottie`) plays when a significant prize is revealed.
- **Sunburst Background**: A dynamic background that enhances the sense of excitement.

### 4. Post-Reveal Actions
- **Re-Roll Dice**: Visible if the user has remaining rolls, allowing them to jump straight back into gameplay.
- **View All Stickers**: Navigates the user to their sticker collection/history.

## Business Logic & State

- **Two-Tap Flow**: First tap opens the box; second tap (or tapping action buttons) proceeds with the next step.
- **Animation Orchestration**: Uses a series of state changes (`showClosedBox` -> `showOpenBox` -> `showGiftCard` -> `showButtons`) to create a satisfying timed sequence.

## API Integration
*Note: This screen primarily displays results fetched after a dice roll or during a grand prize reveal.*

## Navigation
- **Into Prize Reveal**: 
  - Automatically after a winning **Dice Roll**.
  - From the **Monopoly Dashboard** via the floating gift button.
- **Out of Prize Reveal**: 
  - To **Shake Dice**: Tapping "Re-Roll Dice".
  - To **Rewards History**: Tapping "View All Stickers".
  - Dismiss: Controlled via the `onCompletion` callback to ensure the parent screen refresh.
