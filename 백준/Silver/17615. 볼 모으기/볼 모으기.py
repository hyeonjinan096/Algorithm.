import sys
N = int(sys.stdin.readline())
balls = list(sys.stdin.readline().strip())
reversedBalls = balls[::-1]

all_B = balls.count("B")
all_R = balls.count("R")

def check(color):
    front = 0
    while(front < N and balls[front] == color):
        front+=1

    back = 0
    while(back < N and reversedBalls[back] == color):
        back+=1
    return max(front, back)

print(min(all_B-check("B"), all_R-check("R")))
