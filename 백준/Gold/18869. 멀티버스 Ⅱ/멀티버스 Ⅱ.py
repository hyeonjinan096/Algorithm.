import sys
input = sys.stdin.readline

#받기
N, M = map(int,input().split())
dic = dict()

for _ in range(N):
    lst = list(map(int,input().split()))

    new_lst = sorted(lst)

    rank = {new_lst[i]:i for i in range(M)}

    key = tuple(rank[value] for value in lst)  # 튜플 사용 최적화

    if key not in dic:
        dic[key] = 0
    dic[key]+=1

answer = 0
for value in dic.values():
    if value >= 2:
        answer += value * (value-1) // 2

print(answer)