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