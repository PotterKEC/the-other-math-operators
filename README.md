# Python Game Stats Assignment 🎮

## Overview
Welcome to the Python Game Stats Assignment! In this assignment, you'll help build some basic functions that could be used in a game system. You'll practice working with:
- Variables and different data types
- String operations
- Basic math operators (+, *, %)
- Type conversion

## Your Tasks

You need to implement four functions in `assignment.py`:

### 1. `create_player_tag(player_name, player_number)`
Create a player's unique tag by combining their name and number.
- Input: A player name (string) and a number (integer)
- Output: A string with the format "name#number"
- Example: `create_player_tag("Mario", 123)` should return `"Mario#123"`

### 2. `calculate_points_needed(current_score, target_score)`
Calculate how many more points a player needs to reach their target.
- Input: Current score and target score (both integers)
- Output: Points needed (integer)
- Example: `calculate_points_needed(100, 150)` should return `50`

### 3. `create_team_roster(team_size, player_symbol)`
Create a visual representation of the team using symbols.
- Input: Team size (integer) and a symbol (string)
- Output: String with the symbol repeated team_size times
- Example: `create_team_roster(3, "🏃")` should return `"🏃🏃🏃"`

### 4. `distribute_powerups(total_powerups, players_count)`
Calculate leftover powerups after distributing them equally.
- Input: Total powerups and number of players (both integers)
- Output: Number of powerups left over (integer)
- Example: `distribute_powerups(10, 3)` should return `1` (3 players get 3 each, 1 left over)

## Getting Started

1. Clone this repository to your local machine
2. Open `assignment.py` in your favorite Python editor
3. Each function has:
   - A description of what it should do
   - The expected inputs and outputs
   - An example of how it should work
4. Replace each `pass` statement with your code
5. Run the tests to check your work

## Running Tests

To run the tests:

```bash
python -m pytest test_assignment.py
```

The tests will tell you if your functions are working correctly. Make sure all tests pass before submitting!

## Tips for Success

1. Read each function's docstring carefully
2. Look at the example provided for each function
3. Think about edge cases (what if a number is 0? What if a string is empty?)
4. Test your functions with your own examples before running the tests
5. If a test fails, read the error message carefully - it will tell you what went wrong

## What You'll Learn

By completing this assignment, you'll practice:
- Working with variables of different types
- Converting between strings and numbers
- Using string concatenation with the + operator
- Using string repetition with the * operator
- Using the modulo operator % to find remainders
- Writing functions that handle different input cases

## Submission

When you're done:
1. Make sure all tests pass
2. Commit your changes
3. Push your code back to GitHub
4. Submit the link to your repository

Good luck! Remember to have fun while coding! 🎮✨