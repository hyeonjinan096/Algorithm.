lst = [list(map(int,list(input()))) for _ in range(4)]
N = int(input())
turns = [list(map(int,input().split())) for _ in range(N)]

def turn(i,d):
    if d == 1:
        new_lst = [lst[i][7]] +  lst[i][:7]
    else:
        new_lst = lst[i][1:] + [lst[i][0]]

    rev_d = -d

    if i-1 >= 0 and not visited[i-1] and lst[i][6] != lst[i-1][2]:
        visited[i-1] = 1
        turn(i-1, rev_d)

    if i+1 < 4 and not visited[i+1] and lst[i][2] != lst[i+1][6]:
        visited[i+1] = 1
        turn(i+1, rev_d)

    lst[i] = new_lst


for n,d in turns:
    visited = [0]*4
    visited[n-1] = 1
    turn(n-1,d)

score = [1,2,4,8]
answer = 0
for i in range(4):
    answer += lst[i][0] * score[i]

print(answer)