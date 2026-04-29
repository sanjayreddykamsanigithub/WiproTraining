import pytest

@pytest.fixture
def number_list():
    return [1, 2, 3]

def test_list_length(number_list):
    assert len(number_list) == 3