import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


n = int(sys.stdin.readline())
arr = [[0]*n for _ in range(n)] #여기에 앉는 학생 번호 기록

students = [list(map(int, sys.stdin.readline().split())) for _ in range(n**2)]

for m in range(n*n):
    student = students[m]
    tmp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] in student[1:]:
                            like += 1 #좋아하는 친구 있으면 +1
                        if arr[nx][ny] == 0:
                            blank += 1 #비어있는 자리 +1
                tmp.append([like, blank, i, j])
    #like, blank는 클 수록, 행과 열의 수는 작을수록 기준임
    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
    #정렬 후 젤 앞에 있는 리스트의 행과 열의 번호에 학생 앉히기 
    arr[tmp[0][2]][tmp[0][3]] = student[0]

result = 0
## 점수를 매길 때는 학생 순서대로 점수 주기 위해 정렬함 
students.sort()

for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] in students[arr[i][j]-1]:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans-1)
print(result)
