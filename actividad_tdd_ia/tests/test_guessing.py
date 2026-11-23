"""Initial red-phase tests for the guessing game contract."""

import pytest

from game.guessing import calculate_score, check_try


def test_calculate_score_first_attempt_is_100() -> None:
    assert calculate_score(1, True) == 100


def test_check_try_returns_hint_or_correct() -> None:
    assert check_try(40, 50) == "higher"
    assert check_try(60, 50) == "lower"
    assert check_try(50, 50) == "correct"


def test_check_try_rejects_out_of_range_guess() -> None:
    with pytest.raises(ValueError):
        check_try(0, 50)
