# README

## Project Overview

This project is a text-based game where the player faces off against a bot in a series of rounds involving a gun with a mix of live bullets and blanks. The objective is to survive by making strategic decisions on whether to shoot or pass.

## Features

### 1. Title Display
- **File:** `title.py`
- **Function:** `display_title()`
- **Description:** Displays an ASCII art title screen with colored text using ANSI escape codes.

### 2. Player Class
- **File:** `main.py`
- **Class:** `Player`
- **Attributes:**
  - `name`: The name of the player.
  - `lives`: The number of lives the player has (default is 2).
  - `is_bot`: Boolean indicating if the player is a bot (default is `False`).
- **Methods:**
  - `__init__(self, name, is_bot=False)`: Initializes the player with a name and bot status.
  - `shoot(self, chamber)`: Simulates the player shooting. Returns `True` if a live bullet is fired.
  - `lose_life(self)`: Decreases the player's lives by 1.

### 3. Game Rounds
- **File:** `main.py`
- **Function:** `play_game()`
- **Description:** Manages the game rounds, including loading the chamber, handling player and bot actions, and determining the outcome of each round.
- **Rounds Data:** A list of dictionaries specifying the number of blanks and live bullets for each round.

### 4. Chamber Loading
- **File:** `main.py`
- **Function:** `load_chamber(round_data)`
- **Description:** Creates and shuffles the chamber based on the round data, which includes the number of blanks and live bullets.

### 5. Bot Decision Making
- **File:** `main.py`
- **Function:** `bot_decision(chamber)`
- **Description:** Determines the bot's action (shoot or pass) based on the probability of drawing a live bullet from the chamber.

### 6. Game Flow
- **File:** `main.py`
- **Function:** `play_game()`
- **Description:** Controls the flow of the game, including:
  - Displaying round information.
  - Handling player and bot turns.
  - Checking for end-of-round and end-of-game conditions.
  - Displaying appropriate messages based on the game state.

### 7. Start Menu
- **File:** `main.py`
- **Function:** `start_menu()`
- **Description:** Displays the start menu with options to start the game or exit. Calls the `display_title()` function to show the title screen.

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

# Usage

1. **Run the game:**
   `python main.py` 
2. **Follow the on-screen instructions to play the game.**
   
# Dependencies
* colorama: Used for colored text output in the terminal.
  
# License
This project is licensed under the MIT License. See the LICENSE file for more detail
