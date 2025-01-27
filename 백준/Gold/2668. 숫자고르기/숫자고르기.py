N = int(input())
values = [int(input()) -1 for _ in range(N)]
lst = [0]*N
answer = []

def dfs(idx):
    tmp.append(idx)

    if tmp[0] == values[idx]:
        answer.extend(tmp)
        return

    if values[idx] not in tmp and values[idx] not in answer:
        dfs(values[idx])

for idx in range(N):
    tmp = []
    dfs(idx)

answer.sort()
answer = [x+1 for x in answer]
print(len(answer))
print(*answer,sep='\n')