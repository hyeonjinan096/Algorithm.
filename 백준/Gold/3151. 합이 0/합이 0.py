import bisect, sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
answer = 0

for i in range(N-2):
    start = i+1
    end = N-1
    while(start < end):
        result = lst[i] + lst[start] + lst[end]

        if result > 0:
            end -= 1
        else:
            if result == 0:
                if lst[start] == lst[end]:
                    answer += end-start
                else:
                    left = bisect.bisect_left(lst, lst[end])
                    answer += (end - left +1)
            start += 1

print(answer)