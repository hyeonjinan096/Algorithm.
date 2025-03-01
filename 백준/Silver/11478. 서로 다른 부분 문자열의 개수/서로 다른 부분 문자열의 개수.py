s = input()

lst = set()
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        lst.add(s[i:j])

print(len(lst))



