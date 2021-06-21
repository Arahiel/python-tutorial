import pytest

@pytest.fixture
def iterables_source():
    return [
        [1, 2, 3],
        {4, 5, 6},
        (7, 8, 9),
        {"key1": 10, "key2": 11, "key3": 12}
    ]