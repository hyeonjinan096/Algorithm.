import sys
x=int(sys.stdin.readline())

stack = []
stack.append(64)

while(1):
    if sum(stack)>x:
        stack.append(stack.pop()/2)
    elif sum(stack)<x:
        stack.append(stack[-1]/2)
    else:
        print(len(stack))
        break


