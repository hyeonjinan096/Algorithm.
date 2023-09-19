n = int(input())

for i in range(n) :
  m = input()
  if m == "P=NP" : 
    print("skipped")
  else :
    a, b = map(int, m.split('+'))
    print(a + b)