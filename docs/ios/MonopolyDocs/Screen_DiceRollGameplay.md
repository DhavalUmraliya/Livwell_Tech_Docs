# Screen: Dice Roll Gameplay (Shake Dice)

The **Shake Dice** screen is where the actual gameplay happens. It uses device sensors to detect a "shake" motion, which then triggers the dice rolling animation and determines the outcome of the roll.

## Metadata
- **View File**: `MonopolyDiceRoll.swift`
- **ViewModel File**: `DiceRollViewModel.swift`
- **Feature Name**: Shake Dice (Gameplay)

## Key Components

### 1. Navigation & Dice Count
- Shows current **Remaining Dice Rolls**.
- Interactive pop gesture is disabled while dice are animating.

### 2. Dice Area
- Displays a tilting "FrameDice" icon when idle.
- Switches to high-frame-rate animation (`DiceFrameAnimation`) when the user shakes their phone.

### 3. Messaging
- Instruction text: "Shake your phone to roll dice".
- Hidden during animation to avoid clutter.

## Business Logic & State

- **Shake Detection**: Uses `CMMotionManager` to monitor device acceleration. Returns magnitude > 2 for a valid shake.
- **Animation Sequence**: 
  - Play `diceRoll` tone. 
  - Trigger short vibration.
  - Run frame animation for the dice.
  - Call winning determination API on completion.
- **Navigation Callbacks**: Passes success results back to navigation to show "Instant" or "Grand Prize" rewards.

## API Integration

| Action | API Request | Purpose |
| :--- | :--- | :--- |
| Determine Result | `createRequestForFetchingMonopolyWinner` | Finalizes the result of the dice roll (Instant/Grand Prize/Next Time). |

## Navigation
- **Into the Screen**: From the **Monopoly Dashboard** by tapping "Roll Dice".
- **Out of the Screen**: 
  - To **Instant Prize Reveal**: Landing on an instant prize.
  - To **Grand Prize Reveal**: Landing on a sticker or grand prize.
  - To **Better Luck Next Time**: Shown via a custom `DiceRollAlertView`.
  - Manual Close: Tapping the back button (only allowed when not animating).

## Animation Technical Detail
- Uses a sequence of 129 images (`frame_000` to `frame_128`) played at 30 fps using a `Timer` to create a smooth 3D-like dice roll experience.
