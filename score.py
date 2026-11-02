from turtle import Turtle
from paddle import Paddle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor('white')
        self.l_score=0
        self.r_score=0
        
    def display_score(self):
        self.goto(0,230)
        self.write(f'{self.r_score}      {self.l_score}',align='center',font=('courier',50,'bold'))
    def rscore_up(self):
        self.clear()
        self.r_score +=1      
        self.display_score()
    def lscore_up(self):
        self.clear()
        self.l_score +=1
        self.display_score()      
        