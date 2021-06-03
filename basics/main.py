import my_class


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    a = [1, 2, 3]
    b = True
    c = True
    if c and b:
        a = (2, 3)
    print(a[0])
    a = True if b else False
    print(a)
    d = '''a\n
asd'''
    print(d)
    e = {'key1': 1, 'key3': 22}
    for item in e.values():
        print(item)
    e['key2'] = 5
    print(e['key2'])


def call_action_times(action, times):
    print('Started!')
    for i in range(times):
        action(i)
    else:
        print('Finished!')


def loops():
    i = 0
    while i < 5:
        print(i)
        i += 1

    i = 0

    print('\n')

    while True:
        print(i)
        i += 1
        if i >= 5:
            break
    print('\n')


def enter_name_loop():
    min_length = 2

    while True:
        name = input("Please enter the name: ")
        if len(name) >= min_length and name.isprintable() and name.isalpha():
            break;
    print("Hello, {0} ".format(name))


def loop_else():
    x = [1, 2, 3]
    val = 10

    found = False
    idx = 0

    while idx < len(x):
        if x[idx] == val:
            found = True
            break
        idx += 1
    else:
        x.append(val)
    print(x)


def try_statement():  # try..except..finally
    a = 10
    b = 0
    try:
        a / b
    except ZeroDivisionError:
        print("Division by 0")
    finally:
        print("Always executes")
    print("\n")


def try_while_else():
    a = 0
    b = 10
    while a < 4:
        print("---------------------")
        a += 1
        b -= 1

        try:
            a / b
        except ZeroDivisionError:
            print("{0} {1} - division by 0".format(a, b))
            break
        finally:
            print("{0} {1} - always executes".format(a, b))
        print("{0} {1} - main loop".format(a, b))
    else:
        print("No error thrown (no break statement met)")


def for_loop():
    _for_range(range(5))
    _for_range("Hello")
    _for_range(("a", "b", "c", 50))
    _for_range([("a", 1), ("b", 2), ("c", 3)])


def _for_range(iterable):
    for item in iterable:
        print(item)
        try:
            it = iter(item)
            if len(item) <= 1:
                continue
            _for_range(it)
        except TypeError:
            continue
    print("\n")


def for_double_var():
    for i, j in [(1, 2), (3, 4), (4, 5)]:
        print(i, j)


def for_else():
    for i in range(1, 6):
        print(i)
        if i % 7 == 0:
            print("multiple of 7 found")
            break
    else:
        print("no multiples of 7 found")


def for_loop_2():
    s = "hello"
    for i, c in enumerate(s):
        print("{0}:{1}".format(i, c))


if __name__ == '__main__':
    # print_hi('PyCharm')
    # call_action_times(lambda x: print(x), 3)
    # loops()
    # enter_name_loop()
    # loop_else()
    # try_statement()
    # try_while_else()
    # for_loop()
    # for_double_var()
    # for_else()
    # for_loop_2()

    r1 = my_class.Rectangle(10, 20)
    r1.width = 11
    print("Width: ", r1.width)
    print("Area: ", r1.area())
    print("Perimeter: ", r1.perimeter())
    print(str(r1))
    print(repr(r1))

    r2 = my_class.Rectangle(11, 20)
    print("Same references? (r1 is r2): ", r1 is r2)
    print("Same values? (r1 == r2): ", r1 == r2)

    r3 = my_class.Rectangle(10, 30)
    print("{0} is {1}lower than {2}".format("r1", "" if r1 < r3 else "not ", "r3"))

