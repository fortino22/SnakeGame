class Snake:
    
    def __init__(self, height, width):
        self.body = [[height // 2, width // 2]]
        self.direction = None
    
    def move(self):
        head = self.body[0][:] 
        if self.direction == "UP":
            head[0] -= 1
        elif self.direction == "DOWN":
            head[0] += 1
        elif self.direction == "LEFT":
            head[1] -= 1
        elif self.direction == "RIGHT":
            head[1] += 1
        self.body.insert(0, head)
        return head
    
    def set_direction(self, move):
        if move == "w" and self.direction != "DOWN":
            self.direction = "UP"
        elif move == "s" and self.direction != "UP":
            self.direction = "DOWN"
        elif move == "a" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif move == "d" and self.direction != "LEFT":
            self.direction = "RIGHT"
