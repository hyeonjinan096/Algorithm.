import sys

t = int(sys.stdin.readline())

for _ in range(t):

    stick_len, ant_count = map(int, sys.stdin.readline().split())
    min_time = []
    max_time = []

    for _ in range(ant_count):
        loc = int(sys.stdin.readline())
        min_time.append(min(loc, stick_len - loc))
        max_time.append(max(loc, stick_len - loc))

    print(max(min_time), max(max_time))