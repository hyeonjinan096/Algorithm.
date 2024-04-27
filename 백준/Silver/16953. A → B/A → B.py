a,b = map(int, input().split())

answer = -1

def dfs(cur_v,l):
    global answer
    if cur_v > b:
        return
    if cur_v == b:
        answer = l
        return
    dfs(cur_v*2,l+1)
    dfs(cur_v*10+1,l+1)

dfs(a,1)

print(answer)