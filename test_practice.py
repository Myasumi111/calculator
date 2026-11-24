import pytest

def double(number:int) -> int:
    return number * 2

def triple(number: int) -> int:
    return number * 3

def test_triple():
    assert triple(5) == 15

def test_double():
    assert double(4) == 8

def test_addition():
    assert 2 + 3 == 5 # assert = If False, raise error

def test_addition_fail():
    assert 2 + 3 == 6

def test_addition_skip():
    pytest.skip("Not ready yet!")
    assert 2 + 3 == 5

