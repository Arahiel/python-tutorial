from functools import partial
from functools import reduce
from io import TextIOWrapper
from datetime import datetime, timedelta
from module1.my_class import *
from module2.decorators import *

import random
import re


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
            break
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


def basic_methods():
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

    r1 = Rectangle(10, 20)
    r1.width = 11
    print("Width: ", r1.width)
    print("Area: ", r1.area())
    print("Perimeter: ", r1.perimeter())
    print(str(r1))
    print(repr(r1))

    r2 = Rectangle(11, 20)
    print("Same references? (r1 is r2): ", r1 is r2)
    print("Same values? (r1 == r2): ", r1 == r2)

    r3 = Rectangle(10, 30)
    print("{0} is {1}lower than {2}".format(
        "r1", "" if r1 < r3 else "not ", "r3"))


def unpacking():
    l1 = [1, 2, 3, 4]
    l2 = [5, 6, 7]

    # Działa jak SelectMany z C#
    l3 = [*l1, *l2]
    a, *b, c = l1
    print(a, b, c)
    print(l3)


def doc_annotated_function(a: int, b: str) -> str:
    """This is a documentation string"""
    return str(a) + b


def sort():
    l = [2, 5, 4, 6, 8, 9, 10, 1]
    print(l)
    print(sorted(l))


def shuffle():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sorted(l, key=lambda x: random.random()))


# map() działa podobnie jak Select w C#. Przechodzi po *iterables oraz aplikuje podaną funkcję na każdym elemencie.
# Zwraca te same iterables (iterator dokładnie) po zaaplikowaniu funkcji na ich elementach
def map1():
    l = [1, 2, 3]
    print(list(map(lambda x: x ** 2, l)))


# Można podać wiele iterables, bo map(*iterables, l) ma w parametrze gwiazdkę
def map2():
    l = [1, 2, 3]
    k = [4, 5, 6]
    print(list(map(lambda x, y: x + y, l, k)))


# Działa jak Where z C#. Podaje się pojedyncze iterable, oraz predykat. Filter zachowuje elementy, gdy funkcja predykatu
# dla danego elementu zwróci wartość True. Zwraca przefiltrowane iterables (iterator dokładnie)
def filter1():
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(filter(lambda x: x % 2 == 0, l)))


# Łączy elementy ze wszystkich podanych *iterables w tuple
def zip1():
    l = [1, 2, 3]
    k = [4, 5, 6]
    # j = ["p", "y", "t"]
    j = "python"
    print(list(zip(l, k, j)))


# Łączy funkcjonalność map oraz filter.Syntax: newlist = [expression for item in iterable if condition == True].
# IF jest opcjonalny!
def list_comprehension():
    x = [1, 2, 3]
    y = [4, 5, 6]
    print([l + k for l, k in zip(x, y) if k % 2 == 0])

    # Zamiast nawiasów kwadratowych "[]" można użyć normalnych "()", przez co tworzymy generator, a nie listę.
    # Generatory są szybsze od list, gdyż zwracają iterator nie obliczając żadnych elementów (jak IEnumerable w C#).
    # Dopiero po wywołaniu/żądaniu elementu z generatora zostaje on obliczony. Po wywołaniu elementu z generatora
    # iterator się przesuwa, przez co tracimy dostęp do zużytego elementu. Aby go zachować, należy go zapisać
    # np. w liście. Generatory, tak jak IEnumerable są bardzo szybkie, gdyż nie obliczają nic aż do żądania danych.
    for i in (l + k for l, k in zip(x, y) if k % 2 == 0):
        print(i)


# reduce to funkcja agregująca elementy w jeden wynik. W C# to Aggregate z LINQ. Można to przerobić na każdą inną
# funkcję agregującą z C# LINQ, jak np. Sum, Max, Average. Python zawiera wiele wbudowanych funkcji bazujących na
# reduce. Przykłady: min, max, sum, any, all
def reduce1():
    l1 = [1, 2, 3, 4]
    print(reduce(lambda x, y: x + y, l1))  # Sum
    print(sum(l1))  # Built-in Sum
    print(reduce(lambda x, y: x if x > y else y, l1))  # Max


def factory(n):
    # "1" na końcu jest opcjonalną wartością początkową (na początku jest przemnożona (ze wzg. na użytą lambdę) przez
    # pierwszy element z range(1, n + 1)
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


def first_or_default(iterable, predicate):
    # None jest wartością domyślną w przypadku exceptiona
    return next((x for x in iterable if predicate(x)), None)


# Partial służy do redukcji argumentów funkcji
def partial1():
    square = partial(pow, exp=2)
    print(square(3))

    # Jeżeli budujemy partiala przekazując zmienną, to musimy uważać na to, że jeżeli
    # ta zmienna jest immutable - to jej zmiana nie zmieni partiala!
    # ta zmienna jest mutable - to jej zmiana zmieni również wynik partiala
    # polega to na tym, że przekazując zmienna przekazujemy tak naprawdę jej adres, a w przypadku zmiany immutable
    # jej adres się zmienia, ale adres zmiennej przekazanej do partiala nie!

    a = 2  # immutable
    square = partial(pow, exp=a)  # -> 3 ** 2 = 9
    print(square(3))

    a = 3
    print(square(3))  # -> nadal 3 ** 2 = 9


global_var = "GLobal"


def modify_global_var():
    # Użyj globalnej zmiennej zamiast deklarować lokalną o takiej samej nazwie! (shadowing)
    global global_var
    global_var = "GLobal changed!"


c = dict()


def counter_dict(fn, dictionary):
    cnt = 0

    def inner(*args, **kwargs):
        # Użyj zmiennej zadeklarowanej w wyższym scope (nie globalnym!)
        nonlocal cnt
        cnt += 1
        dictionary[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner


def closure_1():
    def mult(a, b):
        return a * b

    def add(a, b):
        return a + b

    counted_add = counter_dict(add, c)
    counted_mult = counter_dict(mult, c)

    print(counted_add(1, 2))
    print(counted_add(2, 2))
    print(counted_mult(5, 2))
    print(c)


# Kolejność dekoratorów ma znaczenie! Im dekorator jest wyżej w kolejności, tym wcześniej się wykonuje, ALE kolejność printów zależy od miejsca wypisania w kodzie
# Jest to syntax działający jak: decorated_add = counter(timed(decorated_add))
# parametr n jest domyślnie ustawiony na n=1
@counter
@timed()  # Sparametryzowany dekorator musi być użyty z nawiasami (nawet z opcjonalnym parametrem)
def decorated_add(a, b):
    return a + b


@timed(5)  # Sparametryzowany dekorator
def fibonacci_reduce(n):
    return reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), range(n), (1, 0))[0]


@DecoratorClass(10, 20)
def cl_decorated(x):
    print("Function: {0}".format(x))


def regex():
    text = """The rain in Spain1;
    The rain in Spain2,
    The rain3 in Spain3."""

    match = re.search("\S+ai\S+", text, re.RegexFlag.MULTILINE)
    print(match.group())

    matches = re.findall("\S+ai\S+", text, re.RegexFlag.MULTILINE)
    print(matches)

    s = list(filter(lambda x: not x.isspace(), re.split(
        r"\s+", text, flags=re.RegexFlag.MULTILINE)))
    print(s)

    result_string = re.sub(
        r"(?<=\s)([a-z])", lambda x: x.group().upper(), text, flags=re.RegexFlag.MULTILINE)
    print(result_string)


def file_handling():
    with open("text.txt", encoding="utf-8", mode="r") as input :
        with open("output.txt", encoding="utf-8", mode="w") as output:
            wait_for_file_to_be_unlocked(output, timedelta(seconds=10))
            for index, line in enumerate( input ):
                output.write(f"{index}: {line.upper()}")

def wait_for_file_to_be_unlocked(file_stream: TextIOWrapper, timeout: timedelta) -> bool:
    """Wait until file is unlocked or timeout is reached.\n
    Returns True if file was unlocked in time."""
    condition = (file_stream.writable() if "w" in file_stream.mode else True) and (file_stream.readable() if "r" in file_stream.mode else True) 
    start = datetime.now()
    timeouted = False

    while not condition:
        condition = (file_stream.writable() if "w" in file_stream.mode else True) and (file_stream.readable() if "r" in file_stream.mode else True)
        end = datetime.now()
        timeouted = end - start >= timeout
        if timeouted:
            break

    if timeouted:
        raise TimeoutError(f"Waiting for file to be unlocked exceeded specified timeout {timeout.seconds}s")


if __name__ == '__main__':
    # basic_methods()
    # unpacking()
    # x = doc_annotated_function(5, "x")
    # sort()
    # shuffle()
    # map1()
    # map2()
    # filter1()
    # zip1()
    # list_comprehension()
    # reduce1()
    # print(factory(6))

    # result = first_or_default([1, 2, 3, 4], lambda x: x > 2)
    # print(result)

    # partial1()

    # modify_global_var()
    # print(global_var)

    # closure_1()

    # print(decorated_add(1, 2))
    # Z użyciem functools.wraps wskazuje na poprawną funkcję. Bez wraps wskazuję niepoprawnie na funkcję inner!
    # help(decorated_add)

    # print(fibonacci_reduce(5))

    # cl_decorated(33)

    # from module1 import my_class
    # print(my_class.value)

    # r = Rectangle(10, 20)
    # print(r.area())
    # r.message("Test message")

    # a = "aaa"
    # print(f"{a}")

    # import my_package
    # print(my_package.subpackage_1.module_1.value)
    # print(my_package.subpackage_2.value)
    # print(my_package.value)  # subpackage_3 value

    # regex()
    file_handling()
