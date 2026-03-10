# Screen: Game Rules & Terms

The **Game Rules** and **Terms & Conditions** screens ensure that users understand how to play the Monopoly game and agree to the legal requirements of participation.

## Metadata
- **View File**: `MonopolyGameRulesView.swift`, `MonopolyTCView.swift`
- **ViewModel File**: `MonopolyGameRulesViewModel.swift`
- **Feature Name**: Game Rules / T&C

## Key Components

### 1. Game Rules List
- Displays a vertical list of rules using `GameRuleCard`.
- Each card includes an icon, a **Key Name** (Title), and a **Value Name** (Description).
- Rules are fetched dynamically from the backend to ensure they are always up-to-date.

### 2. Terms & Conditions (T&C) Bottom Sheet
- A modal view (`MonopolyTCView`) that appears on the **Monopoly Dashboard** for first-time users.
- Includes a summary of rules and an "Accept" button.
- Provides a link to the full Terms & Conditions document via a Safari web view.

## Business Logic & State

- **Dynamic Content**: Both screens use `@Published` properties derived from JSON models (`SMMonopolyGameRulesData`).
- **T&C Enforcement**: The game is locked behind the T&C acceptance logic in `MonopolyHomeUIViewModel`.
- **Analytics**: Both screens track viewing events (`monopolyRulesViewed`, `monopolyTermsAccepted`).

## API Integration

| Action | API Request | Purpose |
| :--- | :--- | :--- |
| Fetch Rules | `createRequestForGetMonopolyGameRules` | Loads the list of rules and regulations. |
| Accept T&C | `createRequestForAcceptMonopolyTC` | Registers the user's acceptance and unlocks the game. |

## Navigation
- **Into Game Rules**: 
  - From **Monopoly Dashboard** via "Game Rules" button.
  - From **Rewards History** via the "?" icon.
- **Out of Game Rules**: 
  - Back to previous screen via the standard navigation back button.
- **T&C Link**: Opens the external terms URL in a `SFSafariViewController`.
