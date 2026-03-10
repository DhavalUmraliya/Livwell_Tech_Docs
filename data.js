const dynamicContent = {
    "ios": {
        "accent": "#007aff",
        "rgb": "0, 122, 255",
        "modules": [
            {
                "title": "Monopoly Login",
                "summary": "The login module handles authentication with Firebase and local biometric storage.",
                "techDocs": "It uses the `LocalAuthentication` framework for biometric checks and `OAuth` for social login.\n\n```swift\nimport MonopolySDK\n\nfunc doLogin() {\n    Monopoly.auth.login()\n}\n```",
                "code": "",
                "lang": "javascript",
                "id": "login",
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