import sys
input = sys.stdin.readline

n,k = map(int,input().split())
lst = list(map(int,input().split()))


s = sum(lst[:k])
answer =s

for i in range(1,n-k+1):
    s = s-lst[i-1]+lst[i+k-1]
    answer = max(answer,s)
print(answer)