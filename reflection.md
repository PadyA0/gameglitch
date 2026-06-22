# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| "-2" | I would expect a warning for crossing the bounds | the game accepted the invalid input | "go lower" |
| clicking "New Game" | new game starting with a fresh history | the "game over" or "new game" banner does not go away | persistent "game over" |
| 7 attempts | 8 tries given for each round | it stops at 7 attempts (0-6) | false advertizing of number of attempts |
| "1000" | rejection of number too high | it accepts entries greater than the upper bound | " go higher" |
| "88" | hint should say to go lower | the banner says go higher when the actual answer is 2 | there is mismatch in the output |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I have used Claude Code in VS Code to explain the code in app.py. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
It pointed out the bugs I noticed while playing without being explicitely prompted to do so. I also used it to refactor parts of the code.  

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
At some point, the agent suggested switching the range in the info text, which was not necessary.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I looked over the new code's logic. Then, I tested the implemention with streamlit.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I used the test file that was refactored, too. The output showed that the code had reversed the game logic. It was erroneous at first, telling the user to go higher when the actual answer was lower, so the game was almost sarcastic.

- Did AI help you design or understand any tests? How?
The AI helped me understand how the scoring worked and how it was faulty because I did not pick up on that during my trials.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
