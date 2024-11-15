import sys
n = int(input())
nums = list(map(int,sys.stdin.readline().split()))
answer = 0
nums.sort()

for i in range(n):
  target = nums[i]
  tmp_nums = nums[:i] + nums[i+1:]

  start, end = 0,n-2
  while(start<end):
    num = tmp_nums[start] + tmp_nums[end]
    if num == target:
      answer+=1
      break
    elif num > target:
      end-=1
    else:
      start+=1

print(answer)
    