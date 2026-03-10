# Screen: Choose Habits (Add Habits)

## Purpose
The Choose Habits screen allows users to discover new habits and add them to their daily tracking list. It provides categorized browsing and a global search feature to help users find habits that align with their health goals.

## Files
- **Views**: 
    - `01ChooseHabitViewUI/HabitTrackingChooseHabitViewUI.swift`
    - `02ChooseHabitSearchViewUI/HabitTrackingChooseHabitSearchViewUI.swift`
- **ViewModel**: `ChooseHabitUIViewModel.swift`
- **Strings**: `ChooseHabitViewUIStrings.swift`

## UI Components
- **Category Tabs**: A horizontal list of habit categories (e.g., Physical, Mental, Nutrition). Selecting a category filters the habit list.
- **Habit Grid/List**: Displays habit cards with name, description, and an "Add" toggle.
- **Search Bar**: Navigates to a dedicated search screen for finding habits by keyword.
- **Active Habit Counter**: Informs the user how many habits are currently in their active list.
- **Next/Save Button**: Confirms the selection of one or more habits and adds them to the user's dashboard.

## Business Logic
- **Category Filtering**: Selecting a category updates `filteredHabitList` with habits belonging specifically to that category.
- **Selection State**: Users can select multiple habits across different categories. The ViewModel tracks these in its internal data structure.
- **Search Logic**: Global search filters the entire `searchHabitList` based on the user's text input.
- **Syncing New Habits**: Clicking "Next" calls the API to persist the newly selected habits. On success, it refreshes the dashboard ViewModel.

## API Integration
- `createRequestForFetchingHabitList`: Retrieves all available habit categories and their corresponding habits.
- `createRequestForCreatingHabitList`: Sends the list of selected habit IDs to the server to be added to the user's profile.

## Navigation
- **Inbound**: From the Habit Dashboard via the "Add Habits" button.
- **Outbound**:
    - **Dashboard**: Returns to the main dashboard after successfully adding habits.
    - **Reminders**: If new habits are added, the user may be prompted to set reminders.
