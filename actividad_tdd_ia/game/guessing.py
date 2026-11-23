"""Contract for the number guessing game."""

import random


def generate_number() -> int:
    """Return a random secret integer between 1 and 100, inclusive."""
    return random.randint(1, 100)


def check_try(guess: int, secret: int) -> str:
    """Compare the player's guess with the secret number.

    Args:
        guess: The player's guess; must be an integer between 1 and 100.
        secret: The secret number to compare the guess against.

    Returns:
        ``"higher"`` when the guess is below the secret, ``"lower"`` when
        the guess is above it, and ``"correct"`` when they match.

    Raises:
        ValueError: If ``guess`` is not an integer between 1 and 100.
    """
    if not isinstance(guess, int) or not 1 <= guess <= 100:
        raise ValueError("guess must be an integer between 1 and 100")
    if not isinstance(secret, int) or not 1 <= secret <= 100:
        raise ValueError("secret must be an integer between 1 and 100")
    if guess < secret:
        return "higher"
    if guess > secret:
        return "lower"
    return "correct"


def calculate_score(attempts: int, won: bool) -> int:
    """Calculate the player's score.

    A lost game scores 0. A won game scores 100 on the first attempt,
    minus 15 points for every extra attempt.

    Args:
        attempts: Number of attempts used.
        won: Whether the player found the secret number.

    Returns:
        The score as an integer.
    """
    if not won:
        return 0
    return 100 - 15 * (attempts - 1)
