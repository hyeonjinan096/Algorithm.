import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

diff = 0
for i in range(1, n+1):
    diff += abs(i - arr[i-1])

print(diff)