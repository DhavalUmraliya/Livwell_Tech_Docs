# Monopoly Localization & Multi-language Support

The Monopoly module is designed to support multiple regions and languages using a combination of local extensions and backend-driven content.

## Localization Mechanism

Static UI strings in the Monopoly module are localized via a custom extension:
- **Usage**: `"string".monopolyLocalised`
- **Supported Languages**: English (default), Vietnamese, and others configured in the app's overall localization system.

## Dynamic Content Localization

Since most game-related descriptions (task names, rewards) are fetched from the API, we use a custom JSON structure to manage translations:

### 1. Model Support (`SMMonopolyTasksList`, `SMMonopolyGameRulesData`)
Models contain language keys (`en`, `vi`, etc.) for each text field.

### 2. Implementation in ViewModel
```swift
self.monopolyGameRules = self.monopolyTaskList.gameTermsCondition.map { item in
    let json = JSON([
        "icon": item.icon,
        "keyName": ["en": item.keyName.en, "vi": item.keyName.vi],
        "valueName": ["en": item.valueName.en, "vi": item.valueName.vi]
    ])
    return SMMonopolyGameRulesData(fromJson: json)
}
```

## Key Localized Strings

| English (en) | Description |
| :--- | :--- |
| **"Roll & Win"** | Dashboard main title. |
| **"Remaining Dice Rolls"** | Count of rolls available to the user. |
| **"Shake your phone to roll dice"** | Gameplay instruction. |
| **"My Gifts"** | Navigation to history. |
| **"Win Big"** | History screen title. |
| **"How you can Win?"** | Step-by-step instructions. |

## Adding New Localized Strings

1. **Add Key**: Define a new key in the app's `Monopoly` localization dictionary.
2. **Translate**: Provide translations for `en` and `vi`.
3. **Use in View**: Call `.monopolyLocalised` on the string key inside the SwiftUI view.

## Localization in Navigation
The `AJNavigationViewUI` takes localized titles but handles back buttons and layout based on the app's global RTL/LTR setting.

## Best Practices
- **Never Hardcode**: Avoid using plain strings; always wrap them in `.monopolyLocalised`.
- **Backend Sync**: Ensure the backend sends the correct language key based on the user's selected language in the app header/profile.
