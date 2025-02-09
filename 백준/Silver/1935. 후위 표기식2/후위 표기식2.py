from collections import deque

N = int(input())
values = list(input())
nums = deque([])
for i in range(N):
    nums.append(int(input()))

stack = deque([])
num_list = dict()
for v in values:
    if 'A'<=v<='Z':
        if v not in num_list:
            num_list[v] = nums.popleft()
        stack.append(num_list[v])
    else:
        a = stack.pop()
        b = stack.pop()
        if v == '-':
            result = b-a
        elif v == '+':
            result = b+a
        elif v == '*':
            result = b*a
        else:
            result = b/a
        stack.append(result)

print("{:.2f}".format(stack[0]))
