Feature: User authentication

Scenario: Sign-in for resources
    Given I am the user username with password password
    When I want to retreive my resource
    Then I should see success message
