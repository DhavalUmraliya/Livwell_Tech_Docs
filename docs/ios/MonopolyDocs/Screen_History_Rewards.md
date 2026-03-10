# Screen: Rewards History (Win Big)

The **Rewards History** screen (titled "Win Big") allows users to track their progress, view collected stickers, and manage their earned prizes.

## Metadata
- **View File**: `MonopolyHistoryViewUi.swift`
- **ViewModel File**: `MonopolyHistoryViewModel.swift`
- **Feature Name**: Win Big (History)

## Key Components

### 1. Tab Segmented Control
- **Stickers**: Displays the puzzle-like sticker collection progress.
- **Prizes**: Shows both grand prizes won and instant gifts collected.

### 2. Sticker Collection Grid
- Uses `MonopolyStickerHistoryCard` to display stickers in a grid.
- Each sticker shows its status (Locked/Revealed) and theme-specific colors.
- Tapping a sticker can reveal more details or the collection status.

### 3. Grand Prizes & Gifts
- **Grand Prizes**: A horizontal scroll of major rewards.
- **Gifts**: A grid of instant prizes (vouchers, points, etc.).
- **View All**: If the user has more than 6 gifts, a "View all" button navigates to `AllInstantGiftUI`.

### 4. Gift Unlock Bottom Sheet
- Tapping a prize opens a `MonopolyGiftUnlockBS` to show collection info or voucher codes.

## Business Logic & State

- **Segment Handling**: Managed via `MonopolySegment` enum.
- **Lock/Unlock Visuals**: Uses opacity (0.5 for locked, 1.0 for revealed/unblocked) to visually distinguish state.
- **Refresh Mechanism**: Standard loading, empty, and error state handling with manual refresh support.

## API Integration

| Action | API Request | Purpose |
| :--- | :--- | :--- |
| Fetch History | `createRequestForMonopolyHistory` | Loads stickers, grand prizes, and gift history. |

## Navigation
- **Into the Screen**: 
  - From **Monopoly Dashboard** via "My Gifts".
  - Automatically after certain rewards are won.
- **Out of the Screen**: 
  - To **Reward Details**: Tapping a gift card opens `AppRouter.openPurchasedRewardDetails`.
  - To **View All Gifts**: Tapping "View all" opens `AllInstantGiftUI`.
  - To **Game Rules**: Tapping "Game Rules" in the navigation bar.
