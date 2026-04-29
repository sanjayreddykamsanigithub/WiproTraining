import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0