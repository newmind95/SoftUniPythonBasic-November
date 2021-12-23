import math

number_of_balls = int(input())
points = 0
total_points = 0
count_red_balls = 0
count_orange_balls = 0
count_yellow_balls = 0
count_white_balls = 0
count_black_balls = 0
count_other_balls = 0

for colors in range(0, number_of_balls):

    color_of_ball = input()

    if color_of_ball == 'red':
        count_red_balls += 1
        points += 5
    elif color_of_ball == 'orange':
        count_orange_balls += 1
        points += 10
    elif color_of_ball == 'yellow':
        count_yellow_balls += 1
        points += 15
    elif color_of_ball == 'white':
        count_white_balls += 1
        points += 20
    elif color_of_ball == 'black':
        count_black_balls += 1
        points = math.floor(points / 2)
    else:
        count_other_balls += 1

total_points = total_points + points

print(f"Total points: {total_points}")
print(f"Red balls: {count_red_balls}")
print(f"Orange balls: {count_orange_balls}")
print(f"Yellow balls: {count_yellow_balls}")
print(f"White balls: {count_white_balls}")
print(f"Other colors picked: {count_other_balls}")
print(f"Divides from black balls: {count_black_balls}")