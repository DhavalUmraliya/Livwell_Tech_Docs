# Insurance Terms View - Technical Documentation

## 1. Executive Summary

**Screen Purpose**: The **Insurance Terms View Activity** (`InsuranceTermsViewUI`) is a dedicated web content viewer. Its sole responsibility is to display external legal documents—such as Terms and Conditions, Disclaimers, and Data Protection Policies—within the app environment without navigating the user to an external browser. This ensures a seamless compliance flow during the purchase process.

**Architecture Pattern**: Pure SwiftUI View. It acts as a wrapper for a `WebViewContainer`, receiving a target URL during initialization.

---

## 2. Screen Flow & Navigation

**Entry Point**:
* **Trigger**: Invoked from the **Insurance Confirm Alert View** (`InsuranceConfirmAlertViewUI`) or **Insurance Package Selection** (`InsurancePackageListViewUI`) when the user taps on a legal link (e.g., "Terms of Use", "Disclaimer", "Policy Wording").

**User Actions**:
1.  **Read Content**: Scroll through the loaded web page to review the legal text.
2.  **Navigate Back**: Tap the "Back" arrow in the navigation header to close the view and return to the previous screen.

---

## 3. UI Components & Layout

**Visual Structure**:
* **Header**: A standard `AJNavigationViewUI` with the title "Terms and Conditions" and a back button action.
* **Web Content**: A `WebViewContainer` (custom component) occupies the majority of the screen space, loading the provided `webURL`.
* **Layout**: Uses a `VStack` with a dark background (`Color(._201E1F)`), ignoring safe areas for an immersive look.

---

## 4. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `init(webURL: URL)` | Initializes the view with the specific legal document URL to load. |
| `WebViewContainer` | A reusable component (likely wrapping `WKWebView`) that renders the HTML content. |
| `popView()` | Dismisses the view using `navigationCoordinator.popView()`. |
