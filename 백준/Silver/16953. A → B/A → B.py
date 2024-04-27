a,b = map(int, input().split())

answer = []

def dfs(cur_v,l):
    global answer
    if cur_v > b:
        return
    if cur_v == b:
        answer.append(l)
        return
    dfs(cur_v*2,l+1)
    dfs(cur_v*10+1,l+1)

dfs(a,1)
if len(answer) ==0:
    print(-1)
else:
    print(min(answer))