# Screen: Streak Dashboard & Activity Details

## Purpose
The Streak Dashboard provides users with a comprehensive overview of their consistency and progress in maintaining habits. It visualizes current streaks, longest streaks, and weekly activity to motivate users to stay on track.

## Files
- **Views**:
    - `04StreakDashboardUI/View/StreakDashboardView.swift`
    - `05StreakActivityDetailsUI/View/StreakActivityDetailsView.swift`
- **ViewModels**:
    - `04StreakDashboardUI/ViewMode/StreakDashboardViewModel.swift`
    - `05StreakActivityDetailsUI/ViewModel/StreakActivityDetailsViewModel.swift`

## UI Components
- **Streak Overview Card**: Displays the current streak count, started date, and user rank.
- **Milestone Progress**: Visual representation of the user's progress toward the next major streak milestone.
- **Weekly Activity Chart**: A vertical or horizontal representation of habit completion for the current week.
- **Longest Streak Stat**: Highlights the user's personal best record for habit consistency.
- **Activity Feed/Details**: In-depth breakdown of habit logs for specific days, accessible via the activity details view.
- **Info Icon**: Opens the `StreakInfoView` which explains how streaks are calculated.

## Business Logic
- **Streak Calculation**: The backend calculates streaks based on daily habit logs. A streak is maintained if at least one habit is completed each day (depending on specific business rules).
- **Ranking**: Users are ranked against others in the community based on their streak consistency, encouraging healthy competition.
- **Historical View**: The activity details screen allows users to scroll through past logs to see their long-term performance trends.

## API Integration
- `createRequestForFetchStreakDashboard`: Retrieves current streak stats, rankings, and weekly activity data.
- `createRequestForFetchStreakActivityDetails`: Fetches the detailed historical log of habit completions.

## Navigation
- **Inbound**: From the Habit Dashboard by tapping the streak header or card.
- **Outbound**:
    - **Streak Info**: Explains the logic behind streak maintenance.
    - **Habit Dashboard**: Returns to the main logging screen for today.
