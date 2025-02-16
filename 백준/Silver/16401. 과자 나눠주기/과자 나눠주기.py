import sys

input = sys.stdin.readline

M, N = map(int, input().split())
values = list(map(int, input().split()))
values.sort(reverse=True)  # 내림차순 정렬하여 불필요한 연산 줄이기

start, end = 1, values[0]
answer = 0

while start <= end:
    mid = (start + end) // 2

    cnt = sum(v // mid for v in values if v >= mid)  # 리스트 컴프리헨션 사용 최적화

    if cnt < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)