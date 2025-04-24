from random import randint

from src.config import (BODY_SIZE, FOOD_COLOR, GAME_HEIGHT, GAME_WIDTH,
                        SNAKE_COLOR, SPACE_SIZE)


class Snake:
    """
    Represents the Snake in the Snake Game.

    Attributes:
        canvas: The game canvas where the snake is drawn.
        direction: The initial direction of the snake's movement ('down' or 'up').
        body_size: The size of the snake's body.
        coordinates: A list of the snake's body segment coordinates.
        squares: A list of the snake's graphical representations (rectangles).
    """
    def __init__(self, direction, canvas):
        self.canvas = canvas
        self.direction = direction
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []

        if self.direction == 'down':
            for _ in range(self.body_size):
                self.coordinates.append([0, 0])
        elif self.direction == 'up':
            for _ in range(self.body_size):
                self.coordinates.append([0, GAME_HEIGHT - SPACE_SIZE])

        for x, y in self.coordinates:
            square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags='snake')
            self.squares.append(square)


class Food:
    """
    Represents the Food in the Snake Game.

    Attributes:
        x: The x-coordinate of the food.
        y: The y-coordinate of the food.
        canvas: The game canvas where the food is drawn.
        coordinates: A list containing the x and y coordinates of the food.
    """
    def __init__(self, snake, canvas):
        while True:
            self.x = randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            self.y = randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            # Make sure the food position does not overlap with snake
            if [self.x, self.y] in snake.coordinates:
                continue
            break

        self.canvas = canvas
        self.coordinates = [self.x, self.y]
        canvas.create_oval(self.x, self.y, self.x + SPACE_SIZE, self.y + SPACE_SIZE, fill=FOOD_COLOR, tag='food')
