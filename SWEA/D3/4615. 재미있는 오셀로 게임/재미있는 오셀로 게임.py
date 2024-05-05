# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''



'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")

T = int(input())
k = [(-1,0),(1,0),(0,1),(0,-1),(-1,1),(1,-1),(-1,-1),(1,1)]

def check(x,y):
    global graph

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    graph = [[0]*n for _ in range(n)]
    M =n//2
    graph[M][M]=graph[M-1][M-1] =2
    graph[M-1][M]=graph[M][M-1] =1
    for i in range(m):
        x,y,d = map(int,input().split())
        x-=1
        y-=1
        graph[x][y] = d
        for j in k:
            dx = x+j[0]
            dy = y+j[1]
            p =[]
            while 0<=dx<n and 0<=dy<n and graph[dx][dy] != 0:
                if graph[dx][dy] !=d:
                    p.append((dx,dy))
                    dx+=j[0]
                    dy+=j[1]
                else:
                    for z in p:
                        graph[z[0]][z[1]] = d
                    break
    white =0
    black =0
    for i in graph:
        for j in i:
            if j == 2: white+=1
            if j == 1: black+=1
    print(f'#{test_case} {black} {white}')