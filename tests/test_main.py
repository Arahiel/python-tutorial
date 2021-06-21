import pytest

def test_always_passes():
    assert True


def test_always_fails():
    assert False

@pytest.mark.basic
# "sequence" and "expected_result" are a parameter names. First argument consists of comma separated strings, which are parameter names.
@pytest.mark.parametrize("sequence, expected_result", [  
    ([1, 2, 3], 1),
    ({4, 5, 6}, 4),
    ((7, 8, 9), 7),
    ({"key1": 10, "key2": 11, "key3": 12}, "key")
])
def test_first_or_default_returns_first_element_in_iterable(sequence, expected_result):
    assert first_or_default(sequence) == expected_result


def first_or_default(iterable, predicate = lambda x: True):  # Duplicate from __main__
    return next((x for x in iterable if predicate(x)), None)


# def test_first_or_default_returns_first_element_in_iterable_fixture_source(iterables_source):
#     for it in iterables_source:
#         assert


@pytest.mark.basic
def test_marked_basic():
    assert 2 > 1


@pytest.mark.skip("Skipped due to...")
def test_skipped():
    assert False
