S,P = map(int,input().split())
lst = list(input())
nums = list(map(int,input().split()))

left = 0
obj = {"A":0 , "C":0,"G":0,"T":0}

def check(obj):
    if obj["A"] >= nums[0] and obj["C"] >= nums[1] and obj["G"] >= nums[2] and obj["T"] >= nums[3]:
        return True

answer=0

for right in range(S):
    obj[lst[right]] += 1

    if right - left + 1 == P:
      if check(obj): 
          answer+=1
      obj[lst[left]] -= 1
      left+=1

print(answer)

    