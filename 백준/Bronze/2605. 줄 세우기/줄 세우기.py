N = int(input())
arr = list(map(int, input().split()))
li = []

for i in range(N):
    if i == 0:
        li.insert(0, i+1)
    else:
        li.insert(arr[i], i+1)

for i in reversed(li):
    print(i, end=" ")