"""Red-phase tests for the main() game loop."""

import builtins

import main
from game import guessing


def _fake_input(answers: list[str], seen: list[str]):
    answers_iterator = iter(answers)

    def fake_input(prompt: str = "") -> str:
        value = next(answers_iterator)
        seen.append(value)
        return value

    return fake_input


def _hint(guess: int, secret: int) -> str:
    if guess == secret:
        return "correct"
    return "higher" if guess < secret else "lower"


def test_main_win_on_first_attempt_reports_score_and_attempts(monkeypatch, capsys) -> None:
    seen: list[str] = []
    monkeypatch.setattr(guessing, "generate_number", lambda: 50)
    monkeypatch.setattr(guessing, "check_try", lambda guess, secret: "correct")
    monkeypatch.setattr(guessing, "calculate_score", lambda attempts, won: 100)
    monkeypatch.setattr(builtins, "input", _fake_input(["50"], seen))

    main.main()

    out = capsys.readouterr().out
    assert "100" in out
    assert "1" in out
    assert seen == ["50"]


def test_main_win_on_third_attempt_reports_score_and_attempts(monkeypatch, capsys) -> None:
    seen: list[str] = []
    monkeypatch.setattr(guessing, "generate_number", lambda: 50)
    monkeypatch.setattr(guessing, "check_try", _hint)
    monkeypatch.setattr(guessing, "calculate_score", lambda attempts, won: 70)
    monkeypatch.setattr(builtins, "input", _fake_input(["40", "60", "50"], seen))

    main.main()

    out = capsys.readouterr().out
    assert "70" in out
    assert "3" in out


def test_main_shows_higher_and_lower_hints_after_wrong_guesses(monkeypatch, capsys) -> None:
    seen: list[str] = []
    monkeypatch.setattr(guessing, "generate_number", lambda: 50)
    monkeypatch.setattr(guessing, "check_try", _hint)
    monkeypatch.setattr(guessing, "calculate_score", lambda attempts, won: 70)
    monkeypatch.setattr(builtins, "input", _fake_input(["40", "60", "50"], seen))

    main.main()

    out = capsys.readouterr().out
    assert "higher" in out
    assert "lower" in out


def test_main_losing_game_reveals_the_secret_number(monkeypatch, capsys) -> None:
    seen: list[str] = []
    monkeypatch.setattr(guessing, "generate_number", lambda: 50)
    monkeypatch.setattr(guessing, "check_try", _hint)
    monkeypatch.setattr(guessing, "calculate_score", lambda attempts, won: 0)
    monkeypatch.setattr(
        builtins, "input", _fake_input(["1", "2", "3", "4", "5", "6", "7"], seen)
    )

    main.main()

    out = capsys.readouterr().out
    assert "50" in out


def test_main_stops_asking_after_seven_attempts(monkeypatch, capsys) -> None:
    seen: list[str] = []
    monkeypatch.setattr(guessing, "generate_number", lambda: 50)
    monkeypatch.setattr(guessing, "check_try", _hint)
    monkeypatch.setattr(guessing, "calculate_score", lambda attempts, won: 0)
    monkeypatch.setattr(
        builtins, "input", _fake_input(["1", "2", "3", "4", "5", "6", "7"], seen)
    )

    main.main()

    capsys.readouterr()
    assert seen == ["1", "2", "3", "4", "5", "6", "7"]


def test_main_invalid_input_shows_message_and_does_not_consume_attempt(
    monkeypatch, capsys
) -> None:
    seen: list[str] = []
    checked: list[int] = []

    def record_check(guess: int, secret: int) -> str:
        checked.append(guess)
        return _hint(guess, secret)

    monkeypatch.setattr(guessing, "generate_number", lambda: 50)
    monkeypatch.setattr(guessing, "check_try", record_check)
    monkeypatch.setattr(guessing, "calculate_score", lambda attempts, won: 100)
    monkeypatch.setattr(builtins, "input", _fake_input(["abc", "50"], seen))

    main.main()

    out = capsys.readouterr().out
    assert "100" in out
    assert "1" in out
    assert checked == [50]
    assert len([line for line in out.splitlines() if line.strip()]) >= 2
