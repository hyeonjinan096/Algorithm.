from sys import stdin

N = int(input())
point = [list(map(int, stdin.readline().split())) for _ in range(N)]
res = float('inf')
sum = 0

def distance(a,b):
    return abs(point[a][0]-point[b][0]) + abs(point[a][1]-point[b][1])

for i in range(N-1):
    sum += distance(i, i+1)

for i in range(1,N-1):
    tmp = sum 
    tmp -= distance(i, i+1) + distance(i, i-1)
    tmp += distance(i-1, i+1)
    res = min(res, tmp)

print(res) 