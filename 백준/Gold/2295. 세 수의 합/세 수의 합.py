import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()

answer = 0
while(answer == 0):
    target = lst.pop()

    for j in range(len(lst)):
        start = j
        end = len(lst)-1
        while(start <= end):
            Sum = lst[j] + lst[start] + lst[end]

            if Sum < target:
                start += 1
            elif Sum > target:
                end -= 1
            else:
                answer = target
                break

print(answer)

