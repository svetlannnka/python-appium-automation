# Created by svetlanalevinsohn at 5/6/23
Feature: Wiki Search tests

  Scenario: User can search on Wikipedia
    Given Click to skip onboarding
    When Click search icon
    And Search for Python (Programming language)
    Then Verify search results shown for Python (programming language)
