s = input()

sum = 0
for i in range(len(s)) :
  if ord(s[i]) >= 97 :
    sum += int(ord(s[i]) - 96)
  else :
    sum += int(ord(s[i]) - 38)

k = 0
for i in range(2, int(sum**0.5) + 1) :
  if sum % i == 0 :
    k = 1

if k == 0 :
  print("It is a prime word.")
else :
  print("It is not a prime word.")