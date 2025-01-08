from collections import deque

N, K = map(int,input().split())
lst = deque(list(map(int,input().split())))
robot = deque([0]*(2*N))
answer = 0

while(1):
    answer+=1

    #회전
    # robot.insert(0,robot.pop())
    # lst.insert(0,lst.pop())
    robot.rotate(1)
    lst.rotate(1)

    #내리기
    robot[N-1] = 0

    #이동(가장 먼저 올라간 것부터)
    i = 0
    # while(i < N-1):
    #     if robot[i] == 1 and robot[i+1] == 0 and lst[i+1] >0:
    #         robot[i], robot[i+1] = 0,1
    #         lst[i+1]-=1
    #         i+=2
    #     else:
    #         i+=1
    for i in range(N-2,-1,-1):
        if robot[i] == 1 and robot[i+1] == 0 and lst[i+1] >0:
            robot[i], robot[i+1] = 0,1
            lst[i+1]-=1

    #내리기
    robot[N-1] = 0

    #올리기
    if lst[0] > 0:
        robot[0] = 1
        lst[0]-=1

    #내구도 검사
    if lst.count(0) >= K:
        break

print(answer)





# 회전로직 -> 배열 안에 1을 한칸씩 옮긴다. 내리는 칸일 경우 없앤다.
# 이동 로직 -> 조건을 만족할 시에 1을 다음 칸에 부여한다.
# 올리는 로직 -> 조건을 만족할 시에 1을 올린다.
# 내구도 검사 로직 -> 내구도 갯수를 파악하고 종료 한다.
# while문을 돌려서 반복한다.

# 배열 에 값을 옮긴다. 이중 배열 [[내구도,로봇 여부],[내구도, 로봇 여부]]
# 회전 pop(), ushift()
# N-1자리이면 1없애버림
# 이동 로직 for문?돌려서 이동 여부 파악??? -1
# 이동 위치에 올려버려 -1
# 내구도 숫자 새
