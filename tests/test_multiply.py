"""
Unit tests for multiply().

You write these on the feature/multiply branch in Lab 03.

Each test below is a STUB: pytest.skip(...) means "don't run this yet".
Replace each pytest.skip(...) line with the real check. The docstring
under each test says what to check.
"""

import pytest

from calculator import multiply


def test_multiply_two_positives() -> None:
    """3 * 4 is 12."""
    assert multiply(3,4) == 12


def test_multiply_by_zero() -> None:
    """Anything times 0 is 0: 9 * 0 is 0."""
    assert multiply(9,0) == 0


# The four sign combinations are the SAME test with different numbers,
# so this one test runs once per row. Each row is (a, b, expected).
# Lab 03 asks you to add the other three rows.
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),  # positive x positive is positive
    (-2, 3, -6),  # Negative x positive is Negative
    (2, -3, -6),  # positive x Negative is Negative
    (-2, -3, 6)   # Negative x Negative is positive  
],
ids = ["+_x_+", "-_x_+","+_x_-","-_x_-"]   )
def test_multiply_signs(a: float, b: float, expected: float) -> None:
    """Positive x positive, both mixed-sign cases, and negative x negative."""
    assert multiply(a,b)  == expected


def test_multiply_floats() -> None:
    """0.1 * 3 is 0.3 - compare with pytest.approx."""
    assert multiply(0.1, 3) == pytest.approx(0.3)
