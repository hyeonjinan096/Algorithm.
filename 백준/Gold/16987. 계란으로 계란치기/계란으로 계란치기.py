N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def dfs(cur_idx, eggs, broken_cnt):
    global answer

    # 최댓값 갱신
    answer = max(answer, broken_cnt)

    # 모든 계란을 다 들었다면 종료
    if cur_idx == N:
        return

    # 현재 계란이 깨져있다면 다음으로 이동
    if eggs[cur_idx][0] <= 0:
        dfs(cur_idx + 1, eggs, broken_cnt)
        return

    is_hit = False  # 칠 수 있는 계란이 있는지 체크

    for i in range(N):
        if i == cur_idx or eggs[i][0] <= 0:
            continue

        is_hit = True

        # 계란 내구도 감소
        eggs[cur_idx][0] -= eggs[i][1]
        eggs[i][0] -= eggs[cur_idx][1]

        # 깨진 계란 수 계산
        new_broken = broken_cnt
        if eggs[cur_idx][0] <= 0:
            new_broken += 1
        if eggs[i][0] <= 0:
            new_broken += 1

        dfs(cur_idx + 1, eggs, new_broken)

        # 상태 복구 (백트래킹)
        eggs[cur_idx][0] += eggs[i][1]
        eggs[i][0] += eggs[cur_idx][1]

    # 칠 수 있는 계란이 없으면 그냥 넘김
    if not is_hit:
        dfs(cur_idx + 1, eggs, broken_cnt)

dfs(0, eggs, 0)
print(answer)
