Feature: Tests for Wiki Search

  Scenario: User can search on Wikipedia
    Given Skip onboarding
    When Click on search icon
    And Search for Python (Programming language)
    Then Verify search result shown for Python (Programming language)