# Habit Tracker Architecture

## Technical Stack
- **Framework**: SwiftUI (primarily) with some UIKit integration where necessary.
- **Pattern**: MVVM (Model-View-ViewModel).
- **Network**: Integrated with `gAPIRequestManager` using `RequestCreator` for API calls.
- **State Management**: Uses `@StateObject` and `@Published` in ViewModels for reactive UI updates.

## Core Components

### 1. View Layer
The views are built using SwiftUI, emphasizing a clean and responsive layout. They are modularized into components (e.g., `HabitCell`, `StreakCard`) to ensure reusability.
- **Entry Points**: `HabitTrackingHomeDashboardViewUI` is the primary entry point.
- **Navigation**: Uses `AJNavigationCoordinator` or standard SwiftUI navigation depending on the context.

### 2. ViewModel Layer
Each major screen has a corresponding ViewModel that inherits from `ObservableObject`.
- **Responsibilities**: 
    - Managing local state (e.g., `addedHabitList`, `notesText`).
    - Handling user interactions (e.g., `updateLogsStatus`, `updateDeleteSelection`).
    - Orchestrating API calls via `RequestCreator`.
    - Parsing JSON responses using `SwiftyJSON`.
- **Key ViewModels**:
    - `HabitTrackingHomeDashboardUIViewModel`: Manages the dashboard state and logs.
    - `AddHabitsUIViewModel`: Manages the habit search and selection logic.
    - `SetHabitReminderUIViewModel`: Manages reminder settings and scheduling.

### 3. Model Layer
Models represent the data structure of habits, dashboards, and API responses.
- **Entities**: 
    - `SMHabit`: Represents a single habit item.
    - `SMHabitDashboard`: Represents the overall dashboard state.
    - `SMHabitsByDate`: Contains habits for a specific calendar day.
    - `SMBaseHabitDashboard`: The root response model from the dashboard API.

## Data Flow
1. **Initial Load**: ViewModel calls `initialSetup()` to determine date ranges and then `callWebServiceForFetchingHabitDashboardList()`.
2. **User Action**: User toggles a habit completion status.
3. **Local Update**: ViewModel updates the `addedHabitList` and sets `isLogStatusChanged = true`.
4. **Sync**: User taps "Keep Moving Forward" (Save), triggering `callWebServiceForLoggingHabitDashboardList()`.
5. **UI Refresh**: On success, the ViewModel parses the new state and updates the `@Published` properties, causing the SwiftUI view to re-render.

## API Integration
The module communicates with the backend through several key endpoints:
- **Fetch Dashboard**: Retrieves the user's habits, streaks, and suggestions.
- **Log Habits**: Synchronizes the completion status of habits for a specific day.
- **Add Habits**: Adds new habits from the catalog to the user's active list.
- **Delete Habits**: Removes habits from the user's active list.
- **Reminders**: Updates notification preferences for habits.
