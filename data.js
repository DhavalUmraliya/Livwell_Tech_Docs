const dynamicContent = {
    "ios": {
        "accent": "#007aff",
        "rgb": "0, 122, 255",
        "modules": [
            {
                "title": "Monopoly API & Data Integration Guide",
                "summary": "This document outlines the networking layer and data models for the Monopoly module.",
                "techDocs": "",
                "code": "",
                "lang": "javascript",
                "id": "api_integration",
                "category": "Monopolydocs"
            },
            {
                "title": "Monopoly Analytics & Event Tracking",
                "summary": "This document specifies the events and properties tracked for MoEngage and CleverTap in the Monopoly module.",
                "techDocs": "",
                "code": "MoEngageManager.trackEvent(key: .roll_dice, \n                           json: [\"dice_left\": self.rewardsDetailsBase.rollDies])\n\nCleverTapManager.shared.track(CleverTapManager.Event.monopolyDiceRolled, \n                              props: [\"dice_left\": self.rewardsDetailsBase.rollDies])",
                "lang": "swift",
                "id": "analytics_tracking",
                "category": "Monopolydocs"
            },
            {
                "title": "Monopoly Architecture Overview",
                "summary": "The **Monopoly** module is built using a clean, modern architecture that bridges new SwiftUI views with existing UIKit infrastructure.",
                "techDocs": "",
                "code": "",
                "lang": "javascript",
                "id": "architecture",
                "category": "Monopolydocs"
            },
            {
                "title": "Monopoly Localization & Multi-language Support",
                "summary": "The Monopoly module is designed to support multiple regions and languages using a combination of local extensions and backend-driven content.",
                "techDocs": "",
                "code": "",
                "lang": "javascript",
                "id": "localization",
                "category": "Monopolydocs"
            },
            {
                "title": "Monopoly Module Overview",
                "summary": "The **Monopoly** module is a gamified feature within the Livwell iOS app that encourages user engagement through tasks, dice rolls, and rewards. It follows a traditional Monopoly board game theme, where users earn \"Roll Dice\" by completing various health and wellness tasks.",
                "techDocs": "- **SwiftUI & UIKit Interop**: Uses modern SwiftUI for most views, integrated with existing UIKit navigation.\n- **MVVM Architecture**: Clean separation of concerns with dedicated ViewModels for each screen.\n- **Real-time Synchronization**: API calls ensure game state (dice rolls, task completion) is always up-to-date with the backend.\n- **Analytics**: Comprehensive tracking of game events via MoEngage and CleverTap.",
                "code": "",
                "lang": "javascript",
                "id": "overview",
                "category": "Monopolydocs"
            },
            {
                "title": "Screen: Dice Roll Gameplay (Shake Dice)",
                "summary": "The **Shake Dice** screen is where the actual gameplay happens. It uses device sensors to detect a \"shake\" motion, which then triggers the dice rolling animation and determines the outcome of the roll.",
                "techDocs": "- Uses a sequence of 129 images (`frame_000` to `frame_128`) played at 30 fps using a `Timer` to create a smooth 3D-like dice roll experience.",
                "code": "",
                "lang": "javascript",
                "id": "screen_dicerollgameplay",
                "category": "Monopolydocs"
            },
            {
                "title": "Screen: Game Rules & Terms",
                "summary": "The **Game Rules** and **Terms & Conditions** screens ensure that users understand how to play the Monopoly game and agree to the legal requirements of participation.",
                "techDocs": "",
                "code": "",
                "lang": "javascript",
                "id": "screen_gamerules_tc",
                "category": "Monopolydocs"
            },
            {
                "title": "Screen: Rewards History (Win Big)",
                "summary": "The **Rewards History** screen (titled \"Win Big\") allows users to track their progress, view collected stickers, and manage their earned prizes.",
                "techDocs": "",
                "code": "",
                "lang": "javascript",
                "id": "screen_history_rewards",
                "category": "Monopolydocs"
            },
            {
                "title": "Screen: Monopoly Dashboard (Roll & Win)",
                "summary": "The **Monopoly Dashboard** is the main screen of the module, where users can view their progress, earn dice through tasks, and initiate gameplay.",
                "techDocs": "",
                "code": "",
                "lang": "javascript",
                "id": "screen_monopolydashboard",
                "category": "Monopolydocs"
            },
            {
                "title": "Screen: Prize Reveal",
                "summary": "The **Prize Reveal** screen is the rewarding climax of the Monopoly experience. It can display an instant reward, a collected sticker (for the grand prize puzzle), or a \"Better Luck Next Time\" message.",
                "techDocs": "",
                "code": "",
                "lang": "javascript",
                "id": "screen_prizereveal",
                "category": "Monopolydocs"
            },
            {
                "title": "Screen: Task Description",
                "summary": "The **Task Description** screen is a detailed bottom-sheet view that provides the user with specific information about a selected task, including the requirements to complete it and the rewards associated with it.",
                "techDocs": "",
                "code": "",
                "lang": "javascript",
                "id": "screen_taskdescription",
                "category": "Monopolydocs"
            },
            {
                "title": "Monopoly State Management & Architecture",
                "summary": "This document details the MVVM implementation and data persistence patterns within the Monopoly module.",
                "techDocs": "",
                "code": "",
                "lang": "javascript",
                "id": "state_management",
                "category": "Monopolydocs"
            },
            {
                "title": "Monopoly Testing & QA Guide",
                "summary": "This document provides a roadmap for testing the Monopoly module, covering primary user flows, edge cases, and simulation tools.",
                "techDocs": "",
                "code": "",
                "lang": "javascript",
                "id": "testing_guide",
                "category": "Monopolydocs"
            },
            {
                "title": "Monopoly Theme & Visual Assets",
                "summary": "The Monopoly module uses a custom color palette and a specific set of visual assets to create a premium gamified experience.",
                "techDocs": "",
                "code": "",
                "lang": "javascript",
                "id": "theme_assets",
                "category": "Monopolydocs"
            }
        ]
    },
    "android": {
        "accent": "#3ddc84",
        "rgb": "61, 220, 132",
        "modules": []
    },
    "web": {
        "accent": "#a855f7",
        "rgb": "168, 85, 247",
        "modules": []
    }
};