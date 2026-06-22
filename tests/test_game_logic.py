import pytest

from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)


# --- get_range_for_difficulty --------------------------------------------

@pytest.mark.parametrize(
    "difficulty, expected",
    [
        ("Easy", (1, 20)),
        ("Normal", (1, 100)),
        ("Hard", (1, 50)),
        ("Unknown", (1, 100)),  # falls back to the default range
    ],
)
def test_get_range_for_difficulty(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected


# --- parse_guess ----------------------------------------------------------

def test_parse_guess_valid_integer():
    assert parse_guess("42") == (True, 42, None)


def test_parse_guess_truncates_float():
    ok, value, err = parse_guess("3.9")
    assert (ok, value, err) == (True, 3, None)


def test_parse_guess_negative():
    assert parse_guess("-7") == (True, -7, None)


@pytest.mark.parametrize("raw", [None, ""])
def test_parse_guess_empty(raw):
    ok, value, err = parse_guess(raw)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


@pytest.mark.parametrize("raw", ["abc", "1,000", "  "])
def test_parse_guess_not_a_number(raw):
    ok, value, err = parse_guess(raw)
    assert ok is False
    assert value is None
    assert err == "That is not a number."


# --- check_guess ----------------------------------------------------------

def test_check_guess_win():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_check_guess_too_high_points_lower():
    # Guess above the secret -> player should aim LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_check_guess_too_low_points_higher():
    # Guess below the secret -> player should aim HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# --- update_score ---------------------------------------------------------

def test_update_score_win_first_attempt_is_full():
    # Winning on attempt 1 awards the full 100 points.
    assert update_score(0, "Win", 1) == 100


def test_update_score_win_decreases_per_attempt():
    # Each extra attempt costs 10 points.
    assert update_score(0, "Win", 3) == 80


def test_update_score_win_floored_at_ten():
    # Late wins never award less than 10 points.
    assert update_score(0, "Win", 50) == 10


@pytest.mark.parametrize("outcome", ["Too High", "Too Low"])
def test_update_score_wrong_guess_costs_five(outcome):
    # A wrong guess always costs 5, regardless of direction or attempt parity.
    assert update_score(100, outcome, 2) == 95
    assert update_score(100, outcome, 3) == 95


def test_update_score_unknown_outcome_unchanged():
    assert update_score(42, "Something", 1) == 42
