@SetVarATo7
Feature: Feature test name

@PrintHelloAfter
Scenario: Scenario name
    Given I print Hello parameter value
      And I print hard-coded Test
     Then I pass test

@PrintHelloBefore
@PrintHelloAfter
Scenario: Scenario name 2 - fail
     When I set var a to 6
     Then Var a is equal to 5
    
@SetVarATo5
Scenario: Scenario name 3 (Var a set up in before tag) - pass
     Then Var a is equal to 5

Scenario: Scenario name 4 - fail
     When I print var a
     Then I fail test

Scenario: Check table parameter
     Then The table contains only even numbers
        |Value|
        |  1  |
        |  2  |
        |  3  |
        |  4  |

Scenario Outline: Scenario Outline name
    Then Check if <Value> is odd
    Examples:
        |Value|
        |  1  |
        |  2  |
        |  3  |
        |  4  |