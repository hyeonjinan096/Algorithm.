N = int(input())
towns = [tuple(map(int, input().split())) for _ in range(N)]
towns.sort()  # x 기준 정렬

total_people = sum(b for x, b in towns)
half_people = (total_people + 1) // 2  # 중앙 이상

acc = 0
for x, b in towns:
    acc += b
    if acc >= half_people:
        print(x)
        break
