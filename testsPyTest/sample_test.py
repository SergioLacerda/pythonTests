import pytest


@pytest.fixture
def expectedResponse():
    return 4

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4
