Feature: UI test cases to help developers identify and fix bugs in the User Interface

  Background:
    Given the URL for environment is "https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a"
    And I enter the website
    When I verify the text "Note - you will need audio in order to get the most out of this game." is present
    And I click the "START" button

  Scenario: The score should be a number between 0 and 100
    When I verify the text "Press on a case to get started." is present
    Then I should see the score is a number between 0 and 100

  Scenario: Burger menu should be present from the Finding the truth page
    When I verify the text "Press on a case to get started." is present
    Then I should see the button "Menu" present
