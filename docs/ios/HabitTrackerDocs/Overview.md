# Habit Tracker Module Overview

## Purpose
The Habit Tracker module in the LivWell application is designed to help users build and maintain healthy habits. It allows users to select from a variety of suggested habits or search for specific ones, track their daily progress, view streaks, and set reminders to stay consistent.

## Key Features
- **Daily Progress Tracking**: Users can log their habits as 'Completed' or 'Skipped' for each day.
- **Streak Management**: Tracks consecutive days of habit completion to provide motivation through streaks.
- **Habit Catalog**: A comprehensive list of habits categorized by focus areas (e.g., Physical, Mental, Lifestyle).
- **Reminders**: Customizable notifications to prompt users to complete their habits.
- **Notes**: Ability to add daily notes to track additional context or reflections on habit progress.
- **Suggested Habits**: Personalized recommendations based on user goals or popular habits.

## User Flow
1. **Entry**: Users enter the Habit Tracker from the Home or Rewards dashboard.
2. **Dashboard**: The main screen shows current streaks and habits for the selected date (defaulting to today).
3. **Logging**: Users tap on a habit to toggle its completion status.
4. **Adding Habits**: Users can tap "Add Habits" to browse the catalog and select new ones.
5. **Managing Habits**: Users can delete habits, edit notes, or set reminders from the dashboard or habit details.
6. **Streaks**: Users can view their streak history and details to understand their long-term progress.

## Module Structure
The module is organized into several sub-views, each handling a specific part of the habit-tracking experience:
- `01HabitTrackingHomeDashboardViewUI`: The central hub for daily tracking.
- `02AddHabitsViews`: Interface for discovering and adding new habits.
- `03SetHabitReminderViewUI`: Configuration for habit-specific reminders.
- `04StreakDashboardUI` & `05StreakActivityDetailsUI`: Visualization of consistency and progress.
- `04EditHabitNotesViewUI`: Detailed note-taking for daily reflections.
