# Screen: Reminders & Notes

## Purpose
This documentation covers the secondary management features of the Habit Tracker: setting reminders to ensure consistency and writing daily notes for reflections.

## Reminders
Reminders help users stay committed by sending notifications at specific times for their chosen habits.

### Files
- **View**: `03SetHabitReminderViewUI/View/SetHabitReminderViewUI.swift`
- **ViewModel**: `03SetHabitReminderViewUI/ViewModel/SetHabitReminderUIViewModel.swift`
- **Popup**: `07SetReminderPopupViewUI/View/SetReminderPopupViewUI.swift`

### Features
- **Global Toggle**: Enable or disable all habit reminders at once.
- **Specific Timing**: Set a daily time for the reminder notification.
- **Habit Specific**: (Optional/Planned) Assign different times to different habits.
- **Local Notifications**: When enabled, the app schedules local notifications via the iOS UserNotifications framework.

## Notes
Notes allow users to record qualitative data about their habit journey, such as why a habit was skipped or how they felt after completing one.

### Files
- **View**: `04EditHabitNotesViewUI/View/EditHabitNotesViewUI.swift`
- **ViewModel**: Managed by the `HabitTrackingHomeDashboardUIViewModel` (via shared state).

### Features
- **Daily Reflection**: Each day has its own note field.
- **Character Limit**: Ensures notes remain concise reflections.
- **Edit/Write States**: Dynamically updates the UI based on whether a note already exists for the day.
- **Persistence**: Notes are synced to the server alongside habit logs when "Keep Moving Forward" is tapped.

## Business Logic
- **Reminder Sync**: When a user changes reminder settings, the app calls `createRequestForSetHabitReminder` to update the backend and then schedules local notification tasks.
- **Note Sync**: Notes are sent in the payload of the `createRequestForLoggingHabitDashboardList` API call.

## Navigation
- **Reminders**: Usually accessed from the Habit Dashboard settings or the "Add Habits" success flow.
- **Notes**: Accessed directly from the Habit Dashboard by clicking "Edit" or "Write" in the notes section.
