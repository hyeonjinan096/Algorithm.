n = int(input())
lst = list(map(int,input().split()))

lst.sort()
mid = len(lst)//2

visited = []
q=[]

def check(a):
    s = 0
    for i in lst:
        s+= abs(i-lst[a])
    return s

def dfs(mid):
    global answer
    if 0<=mid+1<len(lst) and mid+1 not in visited:
        if check(mid+1)<answer[1]:
            visited.append(mid + 1)
            answer[0] = lst[mid + 1]
            answer[1] = check(mid + 1)
            q.append(answer)
            dfs(mid + 1)
        if check(mid+1) == answer[1] and lst[mid+1]<answer[0]:
            visited.append(mid + 1)
            answer[0] = lst[mid + 1]
            answer[1] = check(mid + 1)
            q.append(answer)
            dfs(mid + 1)
    if 0<=mid-1<len(lst) and mid-1 not in visited:
        if check(mid - 1) < answer[1]:
            visited.append(mid - 1)
            answer[0] = lst[mid - 1]
            answer[1] = check(mid - 1)
            q.append(answer)
            dfs(mid - 1)
        if check(mid - 1) == answer[1] and lst[mid - 1] < answer[0]:
            visited.append(mid - 1)
            answer[0] = lst[mid - 1]
            answer[1] = check(mid - 1)
            q.append(answer)
            dfs(mid - 1)

    return

answer = [lst[mid],check(mid)]
q.append(answer)
visited.append(lst[mid])
dfs(mid)

print(answer[0])
