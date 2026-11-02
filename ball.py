from turtle import Turtle,Screen
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.x_cor=10
        self.y_cor=10