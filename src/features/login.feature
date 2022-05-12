Feature: Login feature

    Scenario: Running a login test
        Given I have an account already created
        When I login to goldapp with liis@gmail.com and pass
        Then login is successful