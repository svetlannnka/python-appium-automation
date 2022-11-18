# Created by svetlanalevinsohn at 11/17/22
Feature: Tests for Wikipedia

  Scenario: User can search on Wikipedia
    When Click Skip
    When Click Search Wikipedia
    And Input search query: Python
    Then Verify Python result is shown