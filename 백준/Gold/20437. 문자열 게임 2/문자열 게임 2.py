T = int(input())
for _ in range(T):
    words = list(input())
    K = int(input())
    words_dict = {}
    Max = 0
    Min = float('inf')

    for idx, word in enumerate(words):
        if word not in words_dict:
            words_dict[word] = []
        words_dict[word].append(idx)
        if len(words_dict[word]) == K:
             L = idx - words_dict[word].pop(0)+ 1
             Min = min(Min,L)
             Max = max(Max,L)

    if Min == float('inf') and Max == 0:
        print(-1)
    else:
        print(Min, Max)