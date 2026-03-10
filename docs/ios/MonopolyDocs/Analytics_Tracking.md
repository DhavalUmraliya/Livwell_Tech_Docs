# Monopoly Analytics & Event Tracking

This document specifies the events and properties tracked for MoEngage and CleverTap in the Monopoly module.

## Tracking Managers
The module uses two primary event tracking managers:
- **`MoEngageManager`**: For engagement events.
- **`CleverTapManager`**: For event-based properties and behavioral tracking.

## MoEngage Events

| Event Key | Trigger Context | JSON Metadata (Properties) |
| :--- | :--- | :--- |
| `.monopoly_dashboard` | Dashboard screen loaded. | `no_of_roll_dices` |
| `.roll_dice` | Valid dice roll initiated. | `dice_left` |
| `.reveal_prize` | User reveals a prize (Grand/Instant). | `reveal_prize` (Outcome Type) |

## CleverTap Events

| Event Key | Trigger Context | JSON Metadata (Properties) |
| :--- | :--- | :--- |
| `visitedGame` | Dashboard screen loaded. | `no_of_roll_dices` |
| `monopolyTermsAccepted` | T&C bottom sheet accepted. | - |
| `monopolyGiftClaimed` | Instant prize redeemed. | - |
| `clickedTask` | Task card tapped. | `task_name` |
| `monopolyDiceRolled` | Valid dice roll initiated. | `dice_left` |
| `monopolyHistoryViewed` | History (Win Big) screen loaded. | - |
| `monopolyTabSwitched` | Switched between Stickers and Prizes. | `tab_name` |
| `monopolyRulesViewed` | Game rules screen loaded. | - |

## User-Level Properties (Context)
- **`availableRollDies`**: Current dice count is often passed as a numeric property.
- **`isTermConditionAccepted`**: State is often mirrored in user profiles for segmentation.

## Implementation Pattern
Events are typically tracked within the **ViewModel** after successful API responses or user interactions.

### Example Tracking Code:
```swift
MoEngageManager.trackEvent(key: .roll_dice, 
                           json: ["dice_left": self.rewardsDetailsBase.rollDies])

CleverTapManager.shared.track(CleverTapManager.Event.monopolyDiceRolled, 
                              props: ["dice_left": self.rewardsDetailsBase.rollDies])
```

## Best Practices
- **Localization**: Properties should use English keys for consistency in analytical reports.
- **Timing**: Track events AFTER the UI state transitions to ensure the data persists if the app backgrounded.
