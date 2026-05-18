
# 📘 Assignment: Games in Python

## 🎯 Objective

Build the classic Hangman word-guessing game using Python strings, loops, conditionals, and user input. By the end of this assignment you will have a fully playable terminal game that reinforces core Python programming skills.

## 📝 Tasks

### 🛠️ Word Selection and Display

#### Description
Implement the logic to randomly pick a secret word and display the player's current guessing progress.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list using the `random` module.
- Display the word as underscores (e.g. `_ _ _ _ _`) at the start of the game.
- Reveal correctly guessed letters in their proper positions while keeping unguessed letters as underscores.

### 🛠️ Guess Handling and Game Loop

#### Description
Implement the main game loop that accepts player input, validates guesses, and updates the game state.

#### Requirements
Completed program should:

- Prompt the player to enter a single letter guess each turn.
- Track which letters have already been guessed and notify the player of duplicates.
- Decrement the remaining incorrect guesses counter when a wrong letter is entered.
- Continue the loop until the player either guesses the full word or exhausts all attempts.

### 🛠️ Win / Lose Conditions

#### Description
Detect when the game ends and display an appropriate message to the player.

#### Requirements
Completed program should:

- Display a congratulations message when the player successfully guesses the word.
- Display a game-over message (including the secret word) when the player runs out of attempts.
- Show the number of incorrect guesses remaining after each turn.
