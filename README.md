# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.

This game takes in number guesses from the user. The player has 8 attempts to find the right number that was randomly chosen behind the scenes.

- [ ] Detail which bugs you found.

The bugs I noticed were in the scoring system, the reverse hint logic, and the persistent banners. 

- [ ] Explain what fixes you applied.

The calculations for the scoring was fixed. I added enforcements for boundary checking, so the numbers falling out of range would be dismissed by the game.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 4
2. Game returns "Too Low"
3. User enters a guess of 10 -> Game returns "Too High"
4. Score uodates correctly after each guess
5. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
here are the results of running the test
 python -m pytest
============================================================= test session starts ==============================================================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\padya\vibecoding\game-glitch\gameglitch
plugins: anyio-4.13.0
collected 21 items                                                                                                                              

tests\test_game_logic.py .....................                                                                                            [100%]

============================================================== 21 passed in 0.11s ==============================================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
