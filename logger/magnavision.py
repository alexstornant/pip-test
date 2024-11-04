def hello_world():
    return "Hello, world!"

class Test:
    def __init__(self):
        self.x = 1
        
    def add(self):
        self.x += 1
    
    def sub(self):
        self.x -= 1
        
    def display(self):
        print(self.x)