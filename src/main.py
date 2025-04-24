from src.game_logic import SnakeGame

if __name__ == '__main__':
    snake = SnakeGame()
    snake.move_snake()
    snake.window.mainloop()
