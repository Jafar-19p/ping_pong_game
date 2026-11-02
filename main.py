from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score import Score
window=Screen()
window.tracer(0)
window.setup(800,600)
window.bgcolor('black')
window.title('Ping Pong')
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
window.listen()
window.onkey(r_paddle.up,'Up')
window.onkey(r_paddle.down,'Down')
window.onkey(l_paddle.up,'e')
window.onkey(l_paddle.down,'d')
ball=Ball()
game_on=True
score=Score()
sleep_time=0.1
score.display_score()
while game_on:
  window.update()
  sleep(sleep_time)
  ball.goto(ball.xcor()+ball.x_cor,ball.ycor()+ball.y_cor)
  if ball.ycor() <=-280 or ball.ycor()>280 :
      ball.y_cor*=-1
  if (ball.xcor() <=-330 and ball.distance(l_paddle)<=50 )or (ball.xcor() >=330 and ball.distance(r_paddle)<=50):
      sleep_time*=0.9
      ball.x_cor*=-1
  if ball.xcor()<=-400 :
       ball.goto(0,0)
       ball.x_cor*=-1
       sleep_time=0.1
       score.lscore_up()
  if ball.xcor()>=400 :
        ball.goto(0,0)
        ball.x_cor*=-1
        score.rscore_up()
        sleep_time=0.1

window.exitonclick()