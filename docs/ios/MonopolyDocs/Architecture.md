# Monopoly Architecture Overview

The **Monopoly** module is built using a clean, modern architecture that bridges new SwiftUI views with existing UIKit infrastructure.

## Architecture Pattern

### MVVM (Model-View-ViewModel)
- Each screen consists of:
  - **View**: SwiftUI implementation for layout and visual logic.
  - **ViewModel**: An `ObservableObject` that manages the state, business logic, and API calls.
  - **Model**: SwiftyJSON-powered models for API data parsing.

### Data Flow
1. **View** triggers an action (e.g., dice roll).
2. **ViewModel** calls the backend via `RequestCreator` and `gAPIRequestManager`.
3. **API Success** updates `@Published` properties in the ViewModel.
4. **SwiftUI View** automatically re-renders based on the state changes.

## Integration & Tools

- **Networking**: Uses `RequestCreator` for constructing API requests and `gAPIRequestManager` for execution.
- **Analytics**: Both `MoEngageManager` and `CleverTapManager` are used for tracking game-related events.
- **Navigation**: Managed via a `navigationCoordinator` to ensure seamless transitions between UIKit and SwiftUI environments.
- **Localization**: Leverages `.monopolyLocalised` extensions for multi-language support.

## Key Service Managers

- **MoEngageManager**: Handles push notifications and event tracking for engagement.
- **CleverTapManager**: Tracks user behavior and game events.
- **CommonFunctions**: Utilities for activity loaders, toasts, and more.
