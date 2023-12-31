import sys
import heapq

input = sys.stdin.readline

n = int(input())
presents = []

child = 0

for _ in range(n):
    info = list(map(int, input().split()))

    if info[0] == child:
        if not presents:
            print(-1)   
        else:
            _, present = heapq.heappop(presents)
            print(present)
    else: 
        num, present_info = info[0], info[1:]
        
        for i in range(num):
            heapq.heappush(presents, (-present_info[i], present_info[i]))
