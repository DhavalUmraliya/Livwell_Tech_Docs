# Monopoly Testing & QA Guide

This document provides a roadmap for testing the Monopoly module, covering primary user flows, edge cases, and simulation tools.

## Testing Setup & Simulation

### 1. Developer Testing Mode (`DiceRollViewModel.swift`)
Toggle `TESTING_MODE = true` in `DiceRollViewModel` to simulate winning results without needing a stable backend environment. This avoids using real dice counts.

### 2. Simulator vs. Physical Device
- **Physical Device**: Required for testing **Shake Motion Detection** (`CMMotionManager`).
- **Simulator**: Implements a 2-second timeout fallback that automatically triggers `callWebserviceForMonopolyWinner()` to simulate a shake.

## Manual Test Cases

### 1. First-Time Entry & T&C
- **Scenario**: User enters Monopoly for the first time.
- **Expected**: `MonopolyTCView` bottom sheet is visible. Users cannot interact with the dashboard until "Accept" is tapped.
- **Edge Case**: Tap the "Exit" or "Cancel" button; verify the user is redirected back to the app home.

### 2. Earning Dice via Tasks
- **Scenario**: User taps on a task from the grid.
- **Expected**: `MonopolyTaskDescriptionView` opens, showing details.
- **Action**: Tap the "Join Now" or "Refer a Friend" button; verify correct app navigation.

### 3. Gameplay (Shake to Roll)
- **Scenario**: User has 1+ dice and enters the Shake screen.
- **Action**: Vertically shake the phone.
- **Expected**: `diceRoll` sound plays, phone vibrates, frame animation runs.
- **Edge Case**: Shake with 0 dice. Verify the "No Roll Dice" alert is shown.

### 4. Prize Reveal Flow
- **Scenario**: User lands on a prize.
- **Action**: Tap the bouncing gift box.
- **Expected**: `Sunburst` background appears, box opens, reward is shown.
- **Action**: Tap "Re-Roll Dice". Verify seamless transition back to the Shake screen.

### 5. History & Progress
- **Scenario**: User navigates to "My Gifts".
- **Action**: Switch between "Stickers" and "Prizes" tabs.
- **Expected**: Correct lists are loaded. Locked stickers should be dimmed (50% opacity).

## Edge Case Testing

| Case | Expected Outcome |
| :--- | :--- |
| **No Internet** | Show an error state or toast message with a "Try Again" option. |
| **0 Dice Rolls** | Disable the "Roll Dice" button on the dashboard or show an error toast. |
| **App Killed During Animation** | Upon restart, the dice should be deducted, and the prize should be available in the "History" screen. |
| **Fast Tapping** | Rapid tapping on buttons should be ignored using the `lastTapTime` throttle logic. |

## Visual Quality Assurance (UI/UX)
- Verify that the floating gift button is correctly badged with the count.
- Ensure the `Sunburst` background doesn't clip on different screen sizes (iPhone 7 vs. iPhone 15 Pro).
- Check that long task names don't break the card layouts.
