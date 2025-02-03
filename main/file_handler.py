import os

class FileHandler:
    def __init__(self, file_name="scores.txt"):
        self.file_name = file_name
    
    def write_score(self, user):
        lines = []
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                lines = file.readlines()

        user_exists = False
        for i, line in enumerate(lines):
            try:
                stored_username, stored_password, stored_score = line.strip().split('#')
                if stored_username == user.name:
                    if int(stored_score) < user.score:
                        lines[i] = f"{user.name}#{user.password}#{user.score}\n"
                    user_exists = True
                    break
            except ValueError:
                continue

        if not user_exists:
            lines.append(f"{user.name}#{user.password}#{user.score}\n")

        with open(self.file_name, "w") as file:
            file.writelines(lines)

    def read_scores(self):
        if not os.path.exists(self.file_name):
            return []
        with open(self.file_name, "r") as file:
            return file.readlines()

    def display_scores(self):
        scores = self.read_scores()
        if scores:
            print("{:<20} {:<10}".format("Username", "Score"))
            print("-" * 30)  

            parsed_scores = []
            for score in scores:
                try:
                    stored_username, stored_password, stored_score = score.strip().split('#')
                    parsed_scores.append((stored_username, int(stored_score)))
                except ValueError:
                    continue
            
            parsed_scores.sort(key=lambda x: x[1], reverse=True)
            
            for stored_username, stored_score in parsed_scores:
                print("{:<20} {:<10}".format(stored_username, stored_score))
        else:
            print("No scores recorded yet.")     

    def check_username(self, username):
        scores = self.read_scores()
        for score in scores:
            try:
                stored_username, _, _ = score.strip().split('#')
                if stored_username == username:
                    return True
            except ValueError:
                continue  
        return False

    def get_high_score(self, username):
        scores = self.read_scores()
        highest_score = 0
        for score in scores:
            try:
                stored_username, _, stored_score = score.strip().split('#')
                if stored_username == username:
                    highest_score = max(highest_score, int(stored_score))
            except ValueError:
                continue  
        return highest_score

    def check_password(self, username, password):
        scores = self.read_scores()
        for score in scores:
            try:
                stored_username, stored_password, _ = score.strip().split('#')
                if stored_username == username and stored_password == password:
                    return True
            except ValueError:
                continue  
        return False
    
    def get_password(self, username):
        scores = self.read_scores()
        for score in scores:
            try:
                stored_username, stored_password, _ = score.strip().split('#')
                if stored_username == username:
                    return stored_password  
            except ValueError:
                continue  
        return None
