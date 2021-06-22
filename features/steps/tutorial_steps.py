from behave import *

@given("I print {message} parameter value")
def print_message(context, message):
    print(message)

@given("I print hard-coded Test")
def print_test(context):
    print("Test")

@when("I print var a")
def print_test(context):
    print(f"Var a: {context.a}")

@when("I set var a to {value}")
def set_var_a(context, value):
    context.a = int(value)

@then("I fail test")
def fail_test(context):
    assert False

@then("I pass test")
def pass_test(context):
    assert True

@then("Var a is equal to {expected_value}")
def check_var(context, expected_value):
    assert context.a == int(expected_value), f"Actual: {context.a}, Expected: {expected_value}"

@then("The table contains only even numbers")
def check_table_step_even(context):
    for row in context.table:
        val = int(row["Value"])
        assert val % 2 == 0, f"{val} is not even!"

@then("Check if {value} is odd")
def check_if_value_is_odd(context, value):
    assert int(value) % 2 != 0, f"{value} is not odd!"