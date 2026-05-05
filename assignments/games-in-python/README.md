
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game in Python using strings, loops, conditionals, and user input. By the end of this assignment, you will create a playable game that tracks guesses and clearly reports win or loss outcomes.

## 📝 Tasks

### 🛠️ Create The Core Game Loop

#### Description
Set up the main Hangman gameplay flow. Define a word list, randomly pick one word for each game, and repeatedly prompt the player to guess letters until the game ends.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined Python list.
- Prompt the player for one letter each turn.
- Validate input so only single alphabetic characters are accepted.
- Continue looping until the player wins or runs out of attempts.


### 🛠️ Display Progress And Game Results

#### Description
Show the current puzzle state after each guess and track incorrect attempts remaining. End the game with a clear message that includes the final result.

#### Requirements
Completed program should:

- Display hidden-word progress using underscore placeholders (for example: `_ _ _ _ _`).
- Reveal correctly guessed letters in all matching positions.
- Decrease remaining attempts only for incorrect new guesses.
- Prevent duplicate guessed letters from being counted as new mistakes.
- Print a win message when all letters are guessed.
- Print a lose message when attempts reach zero and reveal the secret word.

```text
Example input/output (abbreviated)

Word: _ _ _ _ _
Guess a letter: a
Correct!
Word: a _ _ _ _
Attempts left: 5

Guess a letter: z
Incorrect.
Word: a _ _ _ _
Attempts left: 4
```
