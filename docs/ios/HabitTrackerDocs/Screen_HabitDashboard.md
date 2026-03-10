# Screen: Habit Tracking Dashboard

## Purpose
The Habit Tracking Dashboard is the primary interface for users to monitor and log their daily habits. It provides a visual representation of current streaks, a date selector for past/future logs, and the list of habits to be completed for the selected day.

## Files
- **View**: `HabitTrackingHomeDashboardViewUI.swift`
- **ViewModel**: `HabitTrackingHomeDashboardUIViewModel.swift`
- **Strings**: `HabitTrackingHomeDashboardViewUIStrings.swift`

## UI Components
- **Streak Header**: Displays the current number of days the user has maintained their habits.
- **Date Selector**: A horizontal scrollable list of dates (last 7 days by default) for selecting which day's habits to view/log.
- **Habit List**: A list of `HabitCell` components showing the habit name, icon, and completion status.
- **Notes Section**: Short snippet of notes for the current day with an "Edit" button.
- **Action Buttons**:
    - **Save (Keep Moving Forward)**: Visible when changes are made to the habit logs.
    - **Delete Icon**: Enables selection mode to remove habits.
    - **Add Habits Button**: Navigates to the habit discovery screen.
- **Suggested Habits**: A horizontal list of recommended habits displayed when the user has few or no active habits.

## Business Logic
- **Date Selection**: Tapping a date updates `lastSelectedDate` and filters `addedHabitList` to show habits for that specific day.
- **Logging**: Tapping a habit cycles its status between `completed`, `skipped`, and `notAttended`. Local changes are tracked via `isLogStatusChanged`.
- **Note Management**: Displays the note for the selected date. Clicking "Edit" opens the `EditHabitNotesViewUI`.
- **Deletion Mode**: Users can toggle a delete mode, select multiple habits, and confirm their removal via an API call.
- **Syncing**: The "Keep Moving Forward" button triggers a bulk update of all habit statuses for the day to the server.

## API Integration
- `createRequestForFetchingHabitDashboardList`: Fetches all data for the dashboard (streaks, habits for the week, suggestions).
- `createRequestForLoggingHabitDashboardList`: Sends the updated completion statuses and notes to the server.
- `createRequestForDeletingHabitList`: Removes one or more selected habits from the user's list.

## Navigation
- **Inbound**: Usually from the Rewards Dashboard or Home screen.
- **Outbound**:
    - `AddHabitsViews`: Via the "Add Habits" button or suggested habit cards.
    - `EditHabitNotesViewUI`: Via the "Edit/Write" notes button.
    - `StreakDashboardUI`: By tapping on the streak header.
    - `SetHabitReminderViewUI`: Accessed via habit settings or the reminder icon.
