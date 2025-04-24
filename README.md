# Snake Game
Welcome to the Snake Game! This is a classic snake game implementation built using Python and Tkinter. The goal of the game is simple: control the snake to collect food while avoiding collisions with the wall or the snake's own body. With every food item consumed, your snake grows longer, making the game more challenging!

## Features
- Simple Gameplay: Easy-to-understand mechanics suitable for all ages.
- Dynamic Direction Control: Navigate the snake using arrow keys.
- Growing Difficulty: The snake grows longer with every food item consumed.
- Game Over Screen: A clean "Game Over!" notification when you lose.
- Restart Option: Easily restart the game without reloading the application.

## Modules
1. `config.py`
Defines the constants and configurations for the game, such as the dimensions, colors, font styles, and game speed.
- Example constants:
    - `GAME_WIDTH`, `GAME_HEIGHT`: Size of the game window.
    - `GAME_SPEED`: Determines the speed of the snake's movement.
    - `SNAKE_COLOR`, `FOOD_COLOR`: Colors for the snake and food.

2. `game_logic.py`
Contains the main logic for running the Snake Game. Key components include:
- `SnakeGame` class: Handles game initialization, snake movements, food interactions, and game-over conditions.
- Game Elements:
    - Canvas for rendering the game environment.
    - Label to display the current score.
    - Restart button to restart the game programmatically.

3. `snake_food.py`
Contains the implementation of the Snake and Food classes.
- `Snake` class:
    - Represents the snake's structure and initial configuration.
    - Handles graphical representation and coordinates of the snake body segments.
- `Food` class:
    - Represents the food object in the game.
    - Randomly spawns on the canvas while avoiding overlap with the snake.

4. `main.py`
Entry point of the application. This script initializes the Snake Game and starts the game loop using mainloop().

## How to Play
1. **Clone the Repository**: Open your terminal and run the following command to clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
```
Replace your-username and your-repo with the actual GitHub username and repository name.

2. Launch the Game:
- Navigate to the main project directory.
- Add the current directory to the `PYTHONPATH` and run the `main.py` script:
```bash
cd Snake_game
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```
3. Control the Snake:
- Use the arrow keys:
    - `Up Arrow`: Move up.
    - `Down Arrow`: Move down.
    - `Left Arrow`: Move left.
    - `Right Arrow`: Move right.
4. Objective:
- Guide the snake to collect food (red ovals) to increase your score.
- Avoid colliding with the walls or your own tail.
5. Game Over:
- When you collide, a "Game Over!" screen will appear.
- Press the "RESTART" button to restart the game.

## Prerequisites
To run this game, you need the following:
- Python 3.x installed on your machine.
- Tkinter (included with Python standard library).
- Random (included with Python standard library).
