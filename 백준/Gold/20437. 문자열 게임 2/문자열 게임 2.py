from collections import deque

T = int(input())
for _ in range(T):
    W = list(input())
    K = int(input())
    Min = float('inf')
    Max = 0
    char_dict = {}

    for idx, val in enumerate(W):
        if val not in char_dict:
            char_dict[val] = deque([])
        char_dict[val].append(idx)

        if len(char_dict[val]) == K:
            L = idx - char_dict[val][0] + 1
            Min = min(L, Min)
            Max = max(L, Max)
            char_dict[val].popleft()

    if Min == float('inf') and Max == 0:
        print(-1)
    else:
        print(Min, Max)