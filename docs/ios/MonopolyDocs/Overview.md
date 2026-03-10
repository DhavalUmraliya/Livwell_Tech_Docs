# Monopoly Module Overview

The **Monopoly** module is a gamified feature within the Livwell iOS app that encourages user engagement through tasks, dice rolls, and rewards. It follows a traditional Monopoly board game theme, where users earn "Roll Dice" by completing various health and wellness tasks.

## Key Features

- **Gamified Tasks**: Integration with daily wellness tasks (Steps, Water intake, Sleep, etc.) to earn dice rolls.
- **Interactive Gameplay**: A virtual board where users roll dice to move through different spaces and claim rewards.
- **Reward System**: Multiple reward types, including instant prizes and a grand prize reveal.
- **History & Progress**: Detailed tracking of earned rewards and game progress.
- **Terms & Rules**: Clear communication of game mechanics and legal disclosures.

## User Flow

1. **Dashboard Entry**: The user enters from the main app dashboard.
2. **Accept Terms**: If it's their first time, they must agree to the Monopoly-specific terms and conditions.
3. **Earn Dice**: Users complete tasks to earn more rolls.
4. **Gameplay**: Users roll dice to move across the board.
5. **Claim Prizes**: Landing on specific spaces triggers rewards or prize reveals.
6. **History**: Users can view their reward history at any time.

## Technical Foundation

- **SwiftUI & UIKit Interop**: Uses modern SwiftUI for most views, integrated with existing UIKit navigation.
- **MVVM Architecture**: Clean separation of concerns with dedicated ViewModels for each screen.
- **Real-time Synchronization**: API calls ensure game state (dice rolls, task completion) is always up-to-date with the backend.
- **Analytics**: Comprehensive tracking of game events via MoEngage and CleverTap.
