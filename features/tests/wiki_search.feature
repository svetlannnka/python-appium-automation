Feature: Tests for search

  Scenario: User can search on Wikipedia
    Given Skip welcome screen
    When Tap Search
    And Search for Python (programming language)
    Then Verify Python (programming language) is shown