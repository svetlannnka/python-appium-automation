Feature: tests for Wikipedia search

  Scenario: User can search on Wikipedia
    Given Click to Skip onboarding
    When Click Search icon
    And Search for Python (programming language)
    Then Verify first result is Python (programming language)