import sys
n = int(input())
nums = list(map(int,sys.stdin.readline().split()))
answer = 0
nums.sort()

for i in range(n):
  target = nums[i]
  tmp_nums = nums[:i] + nums[i+1:]
  
  l, r = 0,n-2
  while(l<r):
    num = tmp_nums[l] + tmp_nums[r] 
    if num == target:
      answer+=1
      break
    elif num>target:
      r -=1
    else:
      l +=1

print(answer)


