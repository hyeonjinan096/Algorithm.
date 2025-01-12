from collections import deque
T = int(input())
for _ in range(T):
    W = list(input())
    K = int(input())
    dic = {}
    Min = float("inf")
    Max = 0

    for idx, val in enumerate(W):
        if val not in dic:
            dic[val] = deque()
        dic[val].append(idx) #idx, level

        if len(dic[val]) == K:
            L = idx - dic[val][0] +1
            Max = max(L,Max)
            Min = min(L,Min)
            dic[val].popleft()


    if (Min == float('inf') and Max == 0):
        print(-1)
    else:
        print(Min, Max)



