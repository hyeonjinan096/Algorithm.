import sys

N, S = map(int, sys.stdin.readline().split())
paintings = dict()
max_height = 0

for _ in range(N):
    H, C = map(int, sys.stdin.readline().split())
    max_height = max(max_height, H)
    if H in paintings:
        paintings[H] = max(paintings[H], C)
    else:
        paintings[H] = C

heights = [0] * (max_height + 1)

for h in range(1, len(heights)):
    if h in paintings:
        new_cost = paintings[h]
        if h-S >= 0:
            new_cost += heights[h-S]
        heights[h] = max(heights[h-1], new_cost)
    else:
        heights[h] = heights[h-1]

print(heights[-1])