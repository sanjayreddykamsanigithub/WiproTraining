import pytest

def square(x):
    return x * x

@pytest.mark.parametrize("num, expected", [
    (2, 4),
    (3, 9),
    (4, 16)
])
def test_square(num, expected):
    assert square(num) == expected
