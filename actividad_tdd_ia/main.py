"""Command-line interface for the number guessing game."""

from game import guessing


def main() -> None:
    """Run one game of 1-100 guessing with at most seven attempts.

    The implementation calls ``guessing.generate_number()`` to create the
    secret, ``guessing.check_try(guess, secret)`` after every valid guess to
    obtain the ``"higher"``/``"lower"``/``"correct"`` hint, and
    ``guessing.calculate_score(attempts, won)`` to obtain the final score.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
