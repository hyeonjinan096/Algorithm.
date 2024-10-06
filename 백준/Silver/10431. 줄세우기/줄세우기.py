from bisect import bisect_left

T = int(input())
for _ in range(T):
  values = list(map(int,input().split()))
  t = values.pop(0)
  answer = 0
  result = []
  for value in values:
    answer += len(result) - bisect_left(result, value)
    result.append(value)
    result.sort()

  print(t, answer, sep = " ") 