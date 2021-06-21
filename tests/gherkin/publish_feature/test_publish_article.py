from pytest_bdd import scenarios, given, when, then

# Point, that steps in this file are able to be executed (start tests with them) from feature files in specified path. 
# In this case it points to root of the app (empty string)
scenarios("") 

@given("I print (.*)")
def print_message(message):
    print(message)

@given("I print hard-coded Test")
def print_test():
    print("Test")

@then("I fail test")
def fail_test():
    assert False

@then("I pass test")
def pass_test():
    assert True