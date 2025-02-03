from game_logic import GameLogic
from file_handler import FileHandler
from user import User
import os
from logo import Logo
import time

import re

class Menu:
    def __init__(self):
        self.file_handler = FileHandler()

    def handle_menu_choice(self):
        while True:
            self.print_ascii()
            print("\n1. Start Game\n2. See HighScore\n3. Exit")
            choice = input("Choose an option: ")
            
            if choice == '1':
                os.system('cls')
                self.start_game()
            elif choice == '2':
                os.system('cls')
                self.file_handler.display_scores()
                input("Press Enter to go back to the main menu...")
                os.system('cls')  
            elif choice == '3':
                os.system('cls')
                logo = Logo()
                logo.clr()
                logo.print_logo()
                print("Exiting game...")
                break
            else:
                print("Invalid choice, please try again.")
                time.sleep(0.5)
                os.system('cls')

    def start_game(self):
        username = self.get_username()
        if username is None:
            return

        if self.file_handler.check_username(username):
            print(f"Welcome back, {username}!")
            while True:
                password = self.get_password(username)
                if password is None:
                    return
                
                stored_password = self.file_handler.get_password(username)
                decoded_password = self.decode_password(stored_password)
                
                if password == decoded_password:
                    break
                else:
                    print("Incorrect password! Please try again.")
                    time.sleep(0.5)
                    os.system('cls')
            
            print(f"Login successful! Your current high score is {self.file_handler.get_high_score(username)}.")

            user = User(username, stored_password)
            user.set_password(stored_password)
        else:
            print(f"Welcome, {username}! Creating a new account.")
            password = self.create_new_account(username)  

            if password is None:
                return
           
        user = User(username, password)
        game = GameLogic(user)
        game.run()

    def get_username(self):
        while True:
            username = input("Enter your username (or press 'q' to quit): ").strip()
            if username.lower() == 'q':
                print("Returning to the main menu...")
                os.system('cls')
                return None
            elif username:
                return username
            else:
                print("Username cannot be empty. Please try again.")
                time.sleep(0.5)
                os.system('cls')

    def get_password(self, username):
        while True:
            password = input("Enter your password (or press 'q' to quit): ").strip()
            if password.lower() == 'q':
                print("Returning to the main menu...")
                os.system('cls')
                return None
            elif self.is_valid_password(password):
                return password
            else:
                print("Password must be at least 6 characters long, contain only alphanumeric characters, and include at least one uppercase letter. Please try again.")
                time.sleep(0.5)
                os.system('cls')

    def create_new_account(self, username):
        while True:
            password = input("Create your password (or press 'q' to cancel): ").strip()
            if password.lower() == 'q':
                print("Account creation cancelled.")
                os.system('cls')
                return
            if self.is_valid_password(password):
                encoded_password = self.encode_password(password)
                user = User(username, encoded_password)
                self.file_handler.write_score(user)
                print(f"Account created for {username}!")
                return encoded_password
            else:
                print("Password must be at least 6 characters long, contain only alphanumeric characters, and include at least one uppercase letter. Please try again.")
                time.sleep(0.5)
                os.system('cls')

    def is_valid_password(self, password):
        if len(password) > 5 and password.isalnum() and re.search(r'[A-Z]', password):
            return True
        return False

    def print_ascii(self):
        print("             _   _                  ______ _____        _                      _                 ")
        print("            | | | |                 |  ___|  _  |      | |                    (_)                ")
        print(" _ __  _   _| |_| |__   ___  _ __   | |_  | | | |_ __  | |__   ___  __ _  __ _ _ _ __   ___ _ __ ")
        print("| '_ \| | | | __| '_ \ / _ \| '_ \  |  _| | | | | '__| | '_ \ / _ \/ _` |/ _` | | '_ \ / _ \ '__|")
        print("| |_) | |_| | |_| | | | (_) | | | | | |   \ \_/ / |    | |_) |  __/ (_| | (_| | | | | |  __/ |   ")
        print("| .__/ \__, |\__|_| |_|\___/|_| |_| \_|    \___/|_|    |_.__/ \___|\__, |\__, |_|_| |_|\___|_|   ")
        print("| |     __/ |                                                       __/ | __/ |                  ")
        print("|_|    |___/                                                       |___/ |___/                   ")

    def encode_password(self, password):
        encoded_password = ''.join(chr(ord(c) + 1) for c in password)
        return encoded_password[::-1]
    
    def decode_password(self, encoded_password):
        decoded_password = ''.join(chr(ord(c) - 1) for c in encoded_password[::-1])
        return decoded_password








































































































 
 
 

 
 
 
 






