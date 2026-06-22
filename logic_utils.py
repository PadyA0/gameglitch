def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: User reported the hint direction was reversed; AI swapped the
    # messages so "too high" tells the player to go LOWER (and vice versa).
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update score based on outcome and attempt number.

    A win on the first attempt is worth the full 100 points; each extra
    attempt costs 10 points, floored at 10. A wrong guess always costs 5
    points, regardless of direction.
    """
    # FIX: User asked to fix scoring; AI corrected the win off-by-one
    # (first-attempt win now scores the full 100, not 80).
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    # FIX: AI removed the attempt-parity bonus so a wrong guess always
    # costs 5, in either direction (confirmed with the user).
    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
