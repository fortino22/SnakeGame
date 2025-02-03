import os
from file_handler import FileHandler

class GenerateMap:
    WIDTH = 30
    HEIGHT = 15
    
    def __init__(self):
        self.board = [[" " for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        self.create_walls()
    
    def create_walls(self):
        for i in range(1, self.WIDTH - 1):
            self.board[0][i] = "═"
            self.board[self.HEIGHT - 1][i] = "═"

        for i in range(1, self.HEIGHT - 1):
            self.board[i][0] = "║"
            self.board[i][self.WIDTH - 1] = "║"

        self.board[0][0] = "╔"
        self.board[0][self.WIDTH - 1] = "╗"
        self.board[self.HEIGHT - 1][0] = "╚"
        self.board[self.HEIGHT - 1][self.WIDTH - 1] = "╝"
    
    def draw(self, snake, food, direction, score):
        os.system("cls" if os.name == "nt" else "clear")
        temp_board = [row[:] for row in self.board]
        temp_board[food[0]][food[1]] = "0"
        
        for segment in snake[1:]:
            temp_board[segment[0]][segment[1]] = "*"
        
        head_icon = {"UP": "^", "DOWN": "v", "LEFT": "<", "RIGHT": ">"}
        temp_board[snake[0][0]][snake[0][1]] = head_icon[direction]
        
        for row in temp_board:
            print("".join(row))

        print(f"Score: {score}")
        print("Controls: W (Up), S (Down), A (Left), D (Right), Q (Quit)")
        print("\n=========================================================")
        print("\nLeaderboard:")

