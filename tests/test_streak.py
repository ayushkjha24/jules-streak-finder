import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test that the function returns the longest of multiple streaks."""
    assert longest_positive_streak([1, 2, -1, 4, 5, 6, 0, 1]) == 3

def test_with_zeros_and_negatives():
    """Test that zeros and negative numbers correctly break streaks."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3
    assert longest_positive_streak([-1, -2, -3]) == 0
    assert longest_positive_streak([0, 0, 0]) == 0

def test_all_positive():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_element_list():
    """Test lists with a single element."""
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([0]) == 0
    assert longest_positive_streak([-1]) == 0

def test_from_description():
    """Test the example from the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3
    assert longest_positive_streak([1, 1, 1]) == 3