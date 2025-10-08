import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_all_positive_numbers():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Test a single streak of positive numbers."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_multiple_streaks_longest_first():
    """Test multiple streaks where the longest streak is first."""
    assert longest_positive_streak([5, 6, 7, 0, 1, 2]) == 3

def test_multiple_streaks_longest_last():
    """Test multiple streaks where the longest streak is last."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, 7]) == 4

def test_streak_with_zeros():
    """Test that zeros correctly break a streak."""
    assert longest_positive_streak([1, 0, 2, 3, 0, 4, 5, 6]) == 3

def test_streak_with_negatives():
    """Test that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, -1, 2, 3, -2, 4, 5, 6]) == 3

def test_streak_of_ones():
    """Test a simple case with a streak of ones."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_example_from_description():
    """Test the primary example from the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3