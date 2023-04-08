import sys
input = sys.stdin.readline

def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif not stack or stack.pop() != p:
            return "NO"
    if(not stack):
        return "YES"
    else:
        return "NO"

n = int(input())
s_list = [input().rstrip() for _ in range(n)]


for i in range(n):
    print(isValid(s_list[i]))
