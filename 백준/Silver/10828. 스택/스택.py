import sys

N = int(input())
stack =[]
for i in range(N):
    S = sys.stdin.readline().split()
    s=S[0]
    if(s =="push"):
        stack.append(S[1])
    elif s=="pop":
        if(not stack):
            print(-1)
        else:
            print(stack.pop())
    elif s=="size":
        print(len(stack))
    elif s=="empty":
        if(not stack):
            print(1)
        else: print(0)
    elif s=="top":
        if(not stack):
            print(-1)
        else:
            print(stack[-1])##

    



