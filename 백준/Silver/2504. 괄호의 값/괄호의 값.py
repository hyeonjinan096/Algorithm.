import sys

def x(s,n):
     if(s ==')'):
          return 2*n
     elif(s==']'):
        return 3*n

def check(s):
    stack = []
    for i in s:
        sum =0    
        if i =='(':
            stack.append(')')
        elif i =='[':
            stack.append(']')
        elif not stack:
            return 0
        elif stack[-1] == i:
            stack.pop()
            if i ==')': stack.append('2')
            else: stack.append('3')
        elif stack[-1] != ')'and stack[-1]!=']':
            if(i not in stack):
                return 0
            while(stack[-1]!=')'and stack[-1]!=']'):
                sum += int(stack.pop())
            if(not stack or stack.pop()!=i):
                return (0)
            stack.append(str(x(i,sum)))
    sum =0
    if(')' in stack or ']' in stack ):
        return (0)
    else:
        while(stack):
            sum +=int(stack.pop())
        return sum
            

s = sys.stdin.readline().strip()

print(check(s))



