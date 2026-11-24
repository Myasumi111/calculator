"""
Unit tests for add().

You write these on the feature/add branch in Lab 02.

Each test below is a STUB. The line pytest.skip(...) tells pytest
"don't run this one yet", so it shows up as an "s" (skipped) instead of
a failure. To write a test, replace its pytest.skip(...) line with the
real check. The docstring under each test says what to check.
"""

import pytest

from calculator import add


def test_add_two_positives() -> None:
    """2 + 3 is 5."""
    a = 2
    b = 3
    expected = 5
    result = add(a,b)
    assert result == expected   


def test_add_negatives() -> None:
    """-4 + -6 is -10."""

    assert add(-4,-6) == -10


def test_add_zero() -> None:
    """Adding 0 changes nothing: 7 + 0 is 7."""
    assert add(7,0) == 7


def test_add_floats() -> None:
    """0.1 + 0.2 is 0.3 - compare with pytest.approx (notebook Section 4)."""
    assert add(0.1, 0.2) == pytest.approx(0.3)
