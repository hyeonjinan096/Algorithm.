import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
left, right = 0, 1

count = 0

while (left <= right and right <= n):
    total = sum(arr[left:right])
    if (total < m):
        right += 1

    elif (total > m):
        left += 1

    else:
        count += 1
        right += 1

print(count)

