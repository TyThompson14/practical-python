# bounce.py
#
# Exercise 1.5

ball_height = 100
bounces = 10
bounce = 1

while bounce <= bounces:
    ball_height = ball_height * (3/5)
    print(bounce, round(ball_height,4))
    bounce = bounce + 1