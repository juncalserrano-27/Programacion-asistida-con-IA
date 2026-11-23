"""Contract for the number guessing game."""


def generate_number() -> int:
    """Return a random secret integer between 1 and 100, inclusive."""
    raise NotImplementedError


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
    raise NotImplementedError


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
    raise NotImplementedError
