Feature: API test cases to help developers identify and fix bugs in the API

  Background:
    Given the URL for environment "test" is "https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a"

  Scenario: Verify Content Security Policy (CSP) header
    When I navigate to the URL
    Then I should see the CSP header

