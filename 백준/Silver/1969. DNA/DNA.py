import sys

N,M = map(int,sys.stdin.readline().strip().split())
arr =[]
for i in range(N):
    arr.append(list(map(str,sys.stdin.readline().strip())))

answer=""
sum = 0
for i in range(M):
    d={"A":0, "C":0, "G":0, "T":0}
    for j in range(N):
        d[arr[j][i]]+=1

    m = max(d,key=d.get)    
    answer+=m
    sum+=(N-d[m])


print(answer)
print(sum)