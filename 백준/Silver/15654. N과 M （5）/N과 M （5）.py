import sys
n, m = map(int,sys.stdin.readline().split())
arr= list(map(int,sys.stdin.readline().split()))

arr.sort()

num =[]

def fun(index):
    if(index ==m):
        print(" ".join(map(str,num)))
        return
    for i in range(n):
        if arr[i] not in num:
            num.append(arr[i])
            fun(index + 1)
            num.pop()

fun(0)