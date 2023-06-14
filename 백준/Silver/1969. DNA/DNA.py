import sys

N,M = map(int,sys.stdin.readline().strip().split())
arr = []
for i in range(N):
    arr.append(list(map(str,sys.stdin.readline().strip())))
    

answer=''
sum =0
for i in range(M):
    map ={"A":0, "C":0,"G":0 ,"T":0}
    for j in range(N):
        map[arr[j][i]] +=1
    m = max(map,key=map.get)
    answer+=m
    sum += (N- map[m])
    map.clear

print(answer)
print(sum)


#answer=[](append)와 answer=""(+=)의 차이를 알것