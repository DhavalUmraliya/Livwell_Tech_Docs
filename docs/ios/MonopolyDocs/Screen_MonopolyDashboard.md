# Screen: Monopoly Dashboard (Roll & Win)

The **Monopoly Dashboard** is the main screen of the module, where users can view their progress, earn dice through tasks, and initiate gameplay.

## Metadata
- **View File**: `MonopolyHomeView.swift`
- **ViewModel File**: `MonopolyHomeUIViewModel.swift`
- **Feature Name**: Roll & Win (Monopoly)

## Key Components

### 1. Hero Banner
- Displays the main event banner.
- Shows total **Available Roll Dice**.
- Provides a "Roll Dice" button that navigates to the **Shake Dice** screen.

### 2. Task Grid
- Displays available tasks in a multi-column horizontal scroll.
- Tasks are categorized and linked to specific wellness activities (Steps, Water, Face Scan, etc.).
- Each task card shows the task title and an icon.

### 3. "How to Win" Section
- Provides step-by-step instructions on how to participate.
- Links to the **Game Rules** screen for detailed mechanics.

### 4. Floating Gift Button
- Appear when a user has a "Grand Gift" to reveal.
- Shows a badge with the count of available grand prize reveals.
- Triggers `callApiForGetMonopolyGrandGift()` when tapped.

## Business Logic & State

- **ViewStatus**: The screen handles multiple states (`loading`, `loaded`, `empty`, `failed`) to provide a robust user experience.
- **Terms & Conditions**: On the first entry, the `MonopolyTCView` bottom sheet is automatically triggered if `isTermConditionAccepted` is false.
- **Data Refresh**: Pull-to-refresh and manual refresh buttons (in empty/error states) trigger `callApiForMonopolyTaskList()`.

## API Integration

| Action | API Request | Purpose |
| :--- | :--- | :--- |
| Fetch Dashboard | `createRequestForGetMonopolyTaskList` | Loads tasks, dice count, banner, and grand prize info. |
| Accept T&C | `createRequestForAcceptMonopolyTC` | Registers user's agreement to the game terms. |
| Reveal Grand Gift | `createRequestForGetMonopolyGrandGift` | Initiates the grand prize reveal process. |

## Navigation
- **Into the Screen**: Usually from the main app dashboard.
- **Out of the Screen**: 
  - To **Shake Dice**: Tapping the "Roll Dice" button.
  - To **History**: Tapping the "My Gifts" button in the navigation bar.
  - To **Game Rules**: Tapping the "Game Rules" button.
  - To **Task Description**: Tapping any task card.
