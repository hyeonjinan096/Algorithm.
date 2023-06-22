import sys

arr = sys.stdin.readline().strip()

A = "z"*len(arr)

for i in range(1,len(arr)-1):
    for j in range(i+1,len(arr)):
        a = arr[:i][::-1]
        b = arr[i:j][::-1]
        c = arr[j:][::-1]
        B =a+b+c
        if(A>B):A=B  #A =min(A,B)

print(A)