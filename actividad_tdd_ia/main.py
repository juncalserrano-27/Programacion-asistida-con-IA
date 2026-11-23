"""Command-line interface for the number guessing game."""

from game import guessing


def main() -> None:
    """Run one game of 1-100 guessing with at most seven attempts.

    The implementation calls ``guessing.generate_number()`` to create the
    secret, ``guessing.check_try(guess, secret)`` after every valid guess to
    obtain the ``"higher"``/``"lower"``/``"correct"`` hint, and
    ``guessing.calculate_score(attempts, won)`` to obtain the final score.
    """
    secret = guessing.generate_number()
    attempts = 0
    won = False
    while attempts < 7:
        text = input("Guess a number between 1 and 100: ")
        if not text.isdigit():
            print("Invalid input: enter an integer between 1 and 100.")
            continue
        guess = int(text)
        attempts += 1
        hint = guessing.check_try(guess, secret)
        print(hint)
        if hint == "correct":
            won = True
            break
    score = guessing.calculate_score(attempts, won)
    print(f"Score: {score}, attempts: {attempts}")
    if not won:
        print(f"The secret number was {secret}.")


if __name__ == "__main__":
    main()
