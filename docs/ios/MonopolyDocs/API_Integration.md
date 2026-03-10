# Monopoly API & Data Integration Guide

This document outlines the networking layer and data models for the Monopoly module.

## Networking Architecture

The Monopoly module uses `RequestCreator` for building requests and `gAPIRequestManager` for execution, following the app's standard API pattern.

### Base Request Creator
Most requests are initiated through the `RequestCreator` class.

## API Endpoints

| Feature | Method | Request Creator Function | Purpose |
| :--- | :--- | :--- | :--- |
| **Dashboard** | GET | `createRequestForGetMonopolyTaskList` | Fetches tasks, dice count, and banner. |
| **T&C** | POST | `createRequestForAcceptMonopolyTC` | Accepts game-specific terms. |
| **Winner** | POST | `createRequestForFetchingMonopolyWinner` | Finalizes dice roll outcome. |
| **Redeem** | POST | `createRequestForGetMonopolyRedeem` | Redeems an instant prize. |
| **History** | GET | `createRequestForGetMonopolyHistory` | Fetches stickers and prize history. |
| **Grand Gift** | GET | `createRequestForGetMonopolyGrandGift` | Initiates grand prize reveal flow. |
| **Rules** | GET | `createRequestForGetMonopolyGameRules` | Fetches game mechanics & rules. |

## Data Models (SwiftyJSON)

The module relies on the following key model hierarchies:

### 1. Dashboard Model (`SMMonopolyDashboardBase`)
- `data`: Contains `tasksList`, `availableRollDies`, `banner`, and `termsConditionLink`.
- `isTermConditionAccepted`: Boolean flag for T&C visibility.
- `isMonopolyEnabled`: Boolean to check if the event is active.

### 2. Rewards Model (`CMMonoPRewardsDetailsBase`)
- `type`: Outcome type (`INSTANT`, `GRAND`, `PRIZZLE`, `BETTER_LUCK_NEXT_TIME`).
- `rollDies`: Remaining dice count after the roll.
- `data`: Reward-specific details (image, name, etc.).

### 3. History Model (`SMMonopolyHistoryBase`)
- `grandPrizeList`: List of stickers for the puzzle.
- `giftList`: List of instant prizes won.
- `stickers`: Categories of stickers collected.

## Error Handling & Status Codes

- **200 OK**: Request successful.
- **400 Bad Request**: Often returned when `availableRollDies` is 0 but a roll is attempted.
- **Other Errors**: Standard network errors are caught and displayed via `CommonFunctions.showToastWithMessage`.

## State Management (`ViewStatus`)
Each ViewModel implements a `ViewStatus` enum to manage UI states:
- `.idle`: Initial state.
- `.loading`: API call in progress.
- `.loaded`: Data successfully received.
- `.empty`: Successful call but no data found.
- `.failed(String)`: Error occurred with a message.
