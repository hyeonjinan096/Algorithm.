N,M = map(int,input().split())
values = list(input().split())
values.sort()

words = ['a','e','i','o','u']
def dfs(i, lst):
    if lst and len(lst) == N:
        cnt = 0
        for j in lst:
            if j in words:
                cnt+=1
        if cnt > 0 and N - cnt > 1:
            print(*lst, sep='')
        return

    if i >= M:
        return

    dfs(i+1,lst + [values[i]])
    dfs(i+1,lst)

dfs(0, [])
