class User:
    def __init__(self, name, password = None, score=0):
        self.name = name
        self.score = 0
        self.password = password  

    def set_score(self, score):
        self.score = score

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password
    
    def check_password(self, password):
        return self.password == password
