import sys


arr=list(map(int,sys.stdin.readline().strip().split()))
arr[2] = abs(arr[0]-arr[2])
arr[3] = abs(arr[1]-arr[3])

print(min(arr))