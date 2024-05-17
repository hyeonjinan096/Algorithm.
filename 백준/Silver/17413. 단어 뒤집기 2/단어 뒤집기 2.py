s = input()
f = '>'
arr=[]
for i in range(len(s)):
    if s[i] == '<' :
        f ='<'
    if f =='<':
        print(s[i],end='')
    if s[i] == '>':
        f = '>'
        continue
    if f=='>' and s[i]== ' ':
        print(s[i],end='')
    if f=='>' and s[i]!= ' ':
        arr.append(s[i])
        if i + 1 == len(s) or s[i + 1] == '<' or s[i + 1] == ' ' :
            arr.reverse()
            print(''.join(arr),end='')
            arr = []


