# Cardio Insurance Questions View - Technical Documentation

## 1\. Executive Summary

**Screen Purpose**: The **Cardio Insurance Questions View** (`CardioInsuranceQuestionsViewUI`) serves as the medical underwriting stage for Cardio Insurance. It presents users with a series of mandatory health questions to determine their eligibility. This screen ensures users declare any pre-existing conditions before proceeding to biometric verification (E-KYC) or being disqualified.

**Architecture Pattern**: MVVM (Model-View-ViewModel). The `CardioInsuranceQuestionsViewUI` observes `CardioInsuranceQuestionsUIViewModel`, which manages the state of questions, user selections, and the completion logic.

-----

## 2\. Screen Flow & Navigation

**Entry Point**:

  * **Trigger**: Invoked from the **Insurance Package Selection** screen (`InsurancePackageListViewUI`) when the user selects a Cardio Insurance package and has not yet completed the questionnaire (`isCardioQuestionarieCompleted == false`).

**User Actions**:

1.  **Read Instructions**: Review the header message: "Please read carefully and check all statements that apply to your medical history".
2.  **Answer Questions**:
      * Scroll through the list of questions.
      * Select an answer (e.g., "Yes", "No") for each question using horizontal option buttons.
3.  **Confirm**: Tap the sticky bottom "Confirm" button.
      * **State**: The button is disabled (`isActive: false`) until all questions have been answered.
      * **Action**: If enabled, tapping it saves the answers to the parent view model (`sharedQuestion`) and sets `sharedQuestionComplete = true`, triggering the eligibility check in the parent flow.
4.  **Navigate Back**: Tap the back button to return to the package selection screen.

-----

## 3\. UI Components & Layout

**Visual Structure**:

  * **Header**: Navigation bar with title "Medical History".
  * **Scrollable Content**:
      * **Header Instruction**: Text block advising careful reading.
      * **Question List**: A vertical stack (`LazyVStack`) rendering each question via `InsuranceQuestionListView`.
      * **Footer Instruction**: An informational block with an "info.circle" icon, warning about the importance of honest answers.
  * **Sticky Footer**: A "Confirm" button pinned to the bottom, managed by `SwiftUICommonViews.bottomButton`.

-----

## 4\. Business Logic & Data Models

### 4.1. Question Management (`InsuranceQuestionListView`)

  * **Display**: Each question row shows the question number (e.g., "Question 1") and the question text.
  * **Selection Logic**:
      * Options are displayed in a horizontal `ScrollView`.
      * Tapping an option toggles its `isSelected` state.
      * **Exclusive Selection**: Selecting one option automatically deselects all others for that specific question.
      * **State Propagation**: Changes are propagated back to the parent ViewModel via the `@Binding var sharedQuestion` and `selectionChanges` toggle.

### 4.2. Completion Validation (`CardioInsuranceQuestionsUIViewModel`)

  * **Logic**: The ViewModel monitors the `selectionChanges` binding. Whenever a selection is made, it runs `hasAllQuestionMarked()`:
    ```swift
    func hasAllQuestionMarked() {
        let allAnswered = questionList.allSatisfy { question in
            question.optionsList.contains { $0.isSelected }
        }
        allQuestionMarked = allAnswered
    }
    ```
  * **Outcome**: Sets `allQuestionMarked`, which enables the "Confirm" button in the UI.

### 4.3. Data Binding

  * The view uses two-way bindings (`@Binding`) for `sharedQuestion` and `sharedQuestionComplete`.
  * This allows the `InsurancePackageListViewUI` (parent) to receive the answers and react immediately when completion is signaled, triggering the eligibility API check (`checkQuestionCerteria`).

-----

## 5\. Key Code Reference

| Component/Method | Purpose |
| :--- | :--- |
| `InsuranceQuestionListView` | Reusable row component for rendering a single question and its options. |
| `hasAllQuestionMarked()` | Validation logic ensuring every question has at least one selected option. |
| `selectionChanges` | A boolean toggle state used to force the ViewModel to re-evaluate validation logic whenever a user taps an option. |
| `sharedQuestionComplete` | Binding that signals the parent view to proceed to the next step (Eligibility Check). |
