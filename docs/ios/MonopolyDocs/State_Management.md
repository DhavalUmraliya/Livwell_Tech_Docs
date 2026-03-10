# Monopoly State Management & Architecture

This document details the MVVM implementation and data persistence patterns within the Monopoly module.

## Core ViewModel Architecture

The module uses `@StateObject` and `@ObservedObject` for a clean, modern data flow.

### 1. `MonopolyHomeUIViewModel` (The Orchestrator)
- **Role**: Manages the dashboard lifecycle, T&C acceptance, and task lists.
- **Key State**:
  - `status: ViewStatus`: Controls the overall screen UI (loading, loaded, empty, failed).
  - `monopolyTaskList: SMMonopolyDashboard`: The primary data source.
  - `showTCBottomSheet: Bool`: Triggers T&C visibility.
- **Persistence**: Most state is derived from API calls; local state is cleared when the view is de-initialized.

### 2. `DiceRollViewModel` (Gameplay)
- **Role**: Manages the sensor-driven gameplay logic and outcomes.
- **Key State**:
  - `isAnimating: Bool`: Disables the back button and interaction during rolls.
  - `remainingRolls: Int`: Tracks the user's available dice count.
  - `prizeType: MonopolyGiftType?`: Stores the result of the current roll.

### 3. `MonopolyHistoryViewModel` (Persistence Layer)
- **Role**: Manages the sticker collection and prize history.
- **Support**: Includes `loadMockData()` to facilitate testing with offline JSON.

## Inter-Component Communication

The module communicates between screens using a mix of SwiftUI and UIKit:

- **Navigation Coordinator**: Uses `navigationCoordinator.pushSwiftUIView` to navigate between views while passing ViewModels or models as dependencies.
- **Callbacks**: Uses `onCompletion` closures to notify parent views when a task is completed (e.g., after a prize reveal).

## Data Synchronization Pattern

1. **Dashboard Fetch**: Initial data load.
2. **Action Trigger**: User rolls dice or completes a task.
3. **API Confirmation**: Backend updates the user's game state.
4. **Local Update**: The ViewModel updates its `@Published` properties, which automatically re-renders the SwiftUI Views.

## Observable Object Patterns

- **`@StateObject`**: Used in main views (Home, History) to manage the primary ViewModel lifecycle.
- **`@ObservedObject`**: Used in sub-components to ensure they stay in sync with the parent data.
- **`@Environment(\.presentationMode)`**: Used for dismissing views and handling back navigation.

## Best Practices
- **Single Source of Truth**: Always derive UI state from the API model where possible.
- **Async Main Threading**: Use `DispatchQueue.mainQueueAsync` for all UI updates inside API callbacks.
- **Memory Management**: Use `[weak self]` in all closures and API callbacks to prevent retain cycles.
