import os
import sys
import random
from tkinter import ALL, Button, Canvas, Label, Tk

from src.config import (BG_COLOR, FONT, GAME_HEIGHT, GAME_OVER_FONT,
                        GAME_SPEED, GAME_WIDTH, SNAKE_COLOR, SPACE_SIZE)
from src.snake_food import Food, Snake


class SnakeGame:
	"""
    A class representing the Snake Game.

    Attributes:
        score: The current game score.
        direction: The direction of snake movement.
        window: The main window of the game.
        label: A label displaying the current score.
        canvas: A canvas for rendering game elements.
        button: A restart button.
		geopetry: Set the initial window position on the screen.
		new_dir: Update the snake direction each time an arrow key is pressed.
        snake: The snake object.
        food: The food object.
    """
	def __init__(self):
		self.score = 0
		self.direction = random.choice(['down', 'up'])
		self.window = self.create_window()
		self.label = self.create_label()
		self.canvas = self.create_canvas()
		self.button = self.create_button()
		self.geometry = self.set_window_position()
		self.new_dir = self.get_new_dir()
		self.snake = Snake(self.direction, self.canvas)
		self.food = Food(self.snake, self.canvas)

	def create_window(self):
		"""
		Create the main game window.

        Return: The game window.
        """
		window = Tk()
		window.title('Snake Game')
		window.resizable(False, False)
		return window

	def create_label(self):
		"""
		Create a label to display the score.

        Return: The score label.
        """
		label = Label(master=self.window, text=f'Score: {self.score}', font=FONT)
		label.pack()
		return label

	def create_canvas(self):
		"""
		Create a canvas for the game elements.

        Return: The game canvas.
        """
		canvas = Canvas(master=self.window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BG_COLOR)
		canvas.pack()
		return canvas

	def create_button(self):
		"""
		Create a restart button.

        Return: The restart button.
        """
		restart_button = Button(master=self.window, bg=BG_COLOR, fg='red', text='RESTART', command=self.restart_program)
		restart_button.pack()

	def set_window_position(self):
		"""Set the initial position of the game window."""
		self.window.update_idletasks()
		window_width = self.window.winfo_width()
		window_height = self.window.winfo_height()
		screen_width = self.window.winfo_screenwidth()
		screen_height = self.window.winfo_screenheight()
		x_offset = (screen_width // 2) - (window_width // 2)
		y_offset = (screen_height // 2) - (window_height // 2)
		self.window.geometry(f'{window_width}x{window_height}+{x_offset}+{y_offset}')

	def change_dir(self, new_dir):
		"""
		Change the direction of the snake.
        """
		if new_dir == 'up':
			if self.direction != 'down':
				self.direction = new_dir
		elif new_dir == 'down':
			if self.direction != 'up':
				self.direction = new_dir
		elif new_dir == 'left':
			if self.direction != 'right':
				self.direction = new_dir
		elif new_dir == 'right':
			if self.direction != 'left':
				self.direction = new_dir

	def get_new_dir(self):
		"""Bind arrow keys to change the snake's direction."""
		self.window.bind('<Up>', lambda event: self.change_dir('up'))
		self.window.bind('<Down>', lambda event: self.change_dir('down'))
		self.window.bind('<Left>', lambda event: self.change_dir('left'))
		self.window.bind('<Right>', lambda event: self.change_dir('right'))

	def check_game_over(self):
		"""
		Check if the game is over.

        Return: True if the game is over, False otherwise.
        """
		x, y = self.snake.coordinates[0]

		if x < 0 or x > GAME_WIDTH:
			return True
		elif y < 0 or y > GAME_HEIGHT:
			return True

		for sq in self.snake.coordinates[1:]:
			if x == sq[0] and y == sq[1]:
				return True
		return False

	def game_over(self):
		"""Display the game over screen."""
		self.canvas.delete(ALL)
		self.canvas.create_text(
			self.canvas.winfo_width() // 2,
			self.canvas.winfo_height() // 2,
			text='Game Over!',
			fill='red',
			font=GAME_OVER_FONT,
		)

	def restart_program(self):
		""" Restarts the program by re-executing the script."""
		path = sys.executable
		os.execv(path, [path] + sys.argv)

	def move_snake(self):
		"""
		Moves the snake in the current direction, checks for food consumption,
        and game-over conditions.
		"""
		x, y = self.snake.coordinates[0]

		if self.direction == 'up':
			y -= SPACE_SIZE
		elif self.direction == 'down':
			y += SPACE_SIZE
		elif self.direction == 'left':
			x -= SPACE_SIZE
		elif self.direction == 'right':
			x += SPACE_SIZE

		self.snake.coordinates.insert(0, [x, y])
		square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
		self.snake.squares.insert(0, square)

		if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
			self.score += 1
			self.label.config(text=f'Score: {self.score}')
			self.canvas.delete('food')
			self.food = Food(self.snake, self.canvas)
		else:
			del self.snake.coordinates[-1]
			self.canvas.delete(self.snake.squares[-1])
			del self.snake.squares[-1]

		if self.check_game_over():
			self.game_over()
		else:
			self.window.after(GAME_SPEED, self.move_snake)
