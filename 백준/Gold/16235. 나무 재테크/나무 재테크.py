import sys
# from collections import deque
input = sys.stdin.readline

N,M,k = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
water = [[5]*N for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]

dir = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
def check_year():
    deadTree = [[0]*N for _ in range(N)]
    # 봄
    for i in range(N):
        for j in range(N):
            new_tree = []
            tree[i][j].sort(reverse=True)
            while len(tree[i][j])>0:
                t = tree[i][j].pop()
                if t > water[i][j]:
                    deadTree[i][j]+=(t//2)
                else:
                    water[i][j] -= t
                    new_tree.append(t+1)

            tree[i][j] = new_tree

    # 여름
    for i in range(N):
        for j in range(N):
            #여름
            if deadTree:
                water[i][j] += deadTree[i][j]

            #겨울
            water[i][j]+=A[i][j]

            #가을
            for t in tree[i][j]:
                if t>0 and t % 5 == 0:
                    for dx,dy in dir:
                        nx = i + dx
                        ny = j+ dy
                        if 0<=nx<N and 0<=ny<N:
                            tree[nx][ny].append(1)

for _ in range(M):
    x,y,a = map(int,input().split())
    x-=1
    y-=1
    tree[x][y].append(a)

for _ in range(k):
    check_year()

answer = 0
for i in range(N):
    for j in range(N):
        answer+=len(tree[i][j])

print(answer)