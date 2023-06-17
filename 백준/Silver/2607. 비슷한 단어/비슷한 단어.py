import sys
N = int(sys.stdin.readline())
arr=[]
for i in range(N):
    arr.append(sys.stdin.readline().strip())

v = list(arr[0])
answer=0

for i in range(1,len(arr)):
    V = v[:] 
    #print("%s+%d"%(arr[i],answer))
    m = arr[i]
    count = 0
    if(len(m) == len(v)):
        for j in m:
            if(j in V):
                 count+=1
                 V.remove(j)
        if(count >=len(m)-1):
            answer+=1

    elif(len(m) ==len(v)-1):
        for j in m:
            if(j in V):
                 count+=1
                 V.remove(j)
        if(count ==len(m)):
            answer+=1

    elif(len(m) == len(v)+1):
        m = list(m)
        for j in v:
            if(j in m): 
                count+=1
                m.remove(j)
        if(count ==len(v)):
            answer+=1

print(answer)
