import random
import time
import sys
import os
import msvcrt
import select
from generate_map import GenerateMap
from snake import Snake
from user import User
from file_handler import FileHandler

class GameLogic:
    DELAY = 0.2
    
    def __init__(self, user=None):  
        self.map = GenerateMap()
        self.snake = Snake(self.map.HEIGHT, self.map.WIDTH)
        self.food = [random.randint(1, self.map.HEIGHT - 2), random.randint(1, self.map.WIDTH - 2)]
        self.score = 0
        self.user = user 

    def get_input(self):
        if self.snake.direction is None:
            print("Press W/A/S/D to start: ", end="", flush=True)
            move = input().strip().lower()
            if move in ["w", "a", "s", "d"]:
                self.snake.set_direction(move)
            else:
                print("Invalid input! Use W/A/S/D to start.")
                return self.get_input()
        
        if os.name == "nt":
            if msvcrt.kbhit():
                move = msvcrt.getch().decode("utf-8").lower()
                if move in ["w", "a", "s", "d"]:
                    self.snake.set_direction(move)
                elif move == "q":
                    self.game_over()
                    exit()
        else:
            print("Press W/A/S/D to change direction, Q to quit: ", end="", flush=True)
            i, o, e = select.select([sys.stdin], [], [], 0)
            if i:
                move = sys.stdin.read(1).strip().lower()
                if move in ["w", "a", "s", "d"]:
                    self.snake.set_direction(move)
                elif move == "q":
                    self.game_over()
                    exit()

    def game_over(self):
        
        print(f"Game Over! Final Score: {self.score}")
        if self.user:
            self.user.set_score(self.score)
            file_handler = FileHandler()
            file_handler.write_score(self.user)  

        print("\nPress 'Enter' to play again or 'Q' to return to the menu.")
        while True:
            if os.name == "nt":  
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode("utf-8").lower()
                    if key == 'q':
                        self.exit_game()
                        break
                    elif key == '\r': 
                        print("Restarting the game...")
                        self.restart_game()
                        break
            else:
                print("Press 'Enter' to play again or 'Q' to return to the menu: ", end="", flush=True)
                i, o, e = select.select([sys.stdin], [], [], 0)
                if i:
                    key = sys.stdin.read(1).strip().lower()
                    if key == 'q':
                        self.exit_game()
                        break
                    elif key == '\r': 
                        print("Restarting the game...")
                        self.restart_game()
                        break

    def restart_game(self):
        self.snake = Snake(self.map.HEIGHT, self.map.WIDTH)
        self.food = [random.randint(1, self.map.HEIGHT - 2), random.randint(1, self.map.WIDTH - 2)]
        self.score = 0
        self.run()  

    def exit_game(self):
        from menu import Menu
        os.system('cls')
        menu = Menu()
        menu.handle_menu_choice()

    def run(self):
        self.get_input()
        while True:
            filehandler = FileHandler()
            
            self.map.draw(self.snake.body, self.food, self.snake.direction, self.score)
            filehandler.display_scores()

            head = self.snake.move()
            
            if head in self.snake.body[1:] or head[0] == 0 or head[0] == self.map.HEIGHT - 1 or head[1] == 0 or head[1] == self.map.WIDTH - 1:
                self.game_over()
                break
            
            if head == self.food:
                self.score += 10
                self.food = [random.randint(1, self.map.HEIGHT - 2), random.randint(1, self.map.WIDTH - 2)]
                self.user.set_score(self.score)
                filehandler.write_score(self.user)
            else:
                self.snake.body.pop()
            
            time.sleep(self.DELAY)
            self.get_input()
