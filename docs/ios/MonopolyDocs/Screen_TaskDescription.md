# Screen: Task Description

The **Task Description** screen is a detailed bottom-sheet view that provides the user with specific information about a selected task, including the requirements to complete it and the rewards associated with it.

## Metadata
- **View File**: `MonopolyTaskDescriptionView.swift`
- **Parent View**: `MonopolyHomeView.swift`
- **Feature Name**: Task Details

## Key Components

### 1. Task Header
- Displays the large **Task Icon** and **Title**.
- Styled with a dark background to match the Monopoly theme.

### 2. Information Blocks
- **"What to do"**: Explains the steps the user needs to take to complete the task.
- **"What you get?"**: Details the rewards (e.g., number of dice rolls) earned upon completion.
- Uses `TaskInfoBlock` for a consistent, card-based layout.

### 3. Action Button
- If the task is enabled, a large **"Join Now"** or **"Refer a Friend"** button is displayed at the bottom.
- Triggers the corresponding app action (e.g., navigating to the referral screen).

## Business Logic & State

- **Drag-to-Dismiss**: Implements a standard iOS bottom-sheet gesture using `DragGesture` and `dragOffset`.
- **Dynamic Content**: Data is populated from the `SMMonopolyTasksList` model passed from the dashboard.
- **Conditional Rendering**: The action button only appears if `task.isEnabled` is true.

## API Integration
*Note: This screen primarily displays data already fetched by the Monopoly Dashboard API.*

## Navigation
- **Into Task Description**: Tap any task card on the **Monopoly Dashboard**.
- **Out of Task Description**: 
  - Drag the sheet down.
  - Tap the dimmed background area.
  - Tap the action button (which also triggers the respective app feature).
