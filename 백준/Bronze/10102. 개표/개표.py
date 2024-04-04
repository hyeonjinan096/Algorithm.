v=int(input())
s=list(input())

if s.count('A')<s.count('B'):
    print('B')
elif s.count('A')>s.count('B'):
    print('A')
else:
    print('Tie')