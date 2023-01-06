import pytest

from hanoi.basics import number_of_positions


# -- Exercise 1* --
# Test the output of def number_of_positions() from hanoi/basics.py, parametrizing over number_of_disks.
@pytest.mark.parametrize("number_of_disks, expected", [(1, 3), (2, 9), (3, 27)])
def test_number_of_positions(number_of_disks: int, expected: int) -> None:
    assert number_of_positions(number_of_disks=number_of_disks) == expected


# -- Exercise 2 --
# What happens to the test_ids of parametrized tests? (Use ```pytest --collect-only```.)
# Find out what "ids" does, when used in pytest.mark.parametrize(... ids= ...).


# -- Exercise 3* --
# Mark all tests in this file with a new mark: "parametrization_paragraph", using only one line of code. Make sure to
# register the mark.


# -- Exercise 4 --
# Create a fixture and parametrize it with two values. Use this fixture to run every test in this paragraph twice
# -without- modifying the tests.
