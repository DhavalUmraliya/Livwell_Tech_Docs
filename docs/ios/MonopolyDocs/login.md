# Monopoly Login
This is the technical documentation for the Monopoly login module on iOS.

## Summary
The login module handles authentication with Firebase and local biometric storage.

## Implementation Details
It uses the `LocalAuthentication` framework for biometric checks and `OAuth` for social login.

```swift
import MonopolySDK

func doLogin() {
    Monopoly.auth.login()
}
```
