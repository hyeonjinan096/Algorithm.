import sys

n,m = map(int,sys.stdin.readline().split())
numbers = [0 for i in range(m)]

def dfs(index):
    if index == m:
        #list 출력함수
        for i in numbers:
            print(i, end = " ")
        print()
        return

    for i in range(1, n+1):
        if i not in numbers:
            numbers[index] = i
            dfs(index + 1)
            numbers[index] = 0

dfs(0)

        




