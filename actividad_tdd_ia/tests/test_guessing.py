"""Red-phase tests for the guessing game functions."""

import pytest

from game.guessing import calculate_score, check_try, generate_number


# Tests from the initial red phase, kept unchanged.


def test_calculate_score_first_attempt_is_100() -> None:
    assert calculate_score(1, True) == 100


def test_check_try_returns_hint_or_correct() -> None:
    assert check_try(40, 50) == "higher"
    assert check_try(60, 50) == "lower"
    assert check_try(50, 50) == "correct"


def test_check_try_rejects_out_of_range_guess() -> None:
    with pytest.raises(ValueError):
        check_try(0, 50)


# generate_number: returns an int between 1 and 100, inclusive.


def test_generate_number_returns_an_integer() -> None:
    assert isinstance(generate_number(), int)


@pytest.mark.parametrize("_draw", range(5))
def test_generate_number_is_within_one_and_one_hundred(_draw: int) -> None:
    assert 1 <= generate_number() <= 100


# check_try: accepted values produce the specified hint.


@pytest.mark.parametrize(
    ("guess", "secret", "expected"),
    [
        (1, 100, "higher"),
        (100, 1, "lower"),
        (1, 1, "correct"),
        (100, 100, "correct"),
        (50, 50, "correct"),
    ],
)
def test_check_try_returns_expected_hint(
    guess: int, secret: int, expected: str
) -> None:
    assert check_try(guess, secret) == expected


# check_try: only integers between 1 and 100 are accepted.


@pytest.mark.parametrize("guess", [0, 101, -1, -100, 50.5, "50"])
def test_check_try_rejects_invalid_guess(guess: int | float | str) -> None:
    with pytest.raises(ValueError):
        check_try(guess, 50)


@pytest.mark.parametrize("secret", [0, 101, -5, 50.5])
def test_check_try_rejects_invalid_secret(secret: int | float) -> None:
    with pytest.raises(ValueError):
        check_try(50, secret)


# calculate_score: 100 on the first won attempt, minus 15 per extra attempt.


@pytest.mark.parametrize(
    ("attempts", "expected"),
    [
        (1, 100),
        (2, 85),
        (7, 10),
    ],
)
def test_calculate_score_winning_score_matches_spec(attempts: int, expected: int) -> None:
    assert calculate_score(attempts, True) == expected


@pytest.mark.parametrize("attempts", [1, 7])
def test_calculate_score_lost_game_returns_zero(attempts: int) -> None:
    assert calculate_score(attempts, False) == 0
