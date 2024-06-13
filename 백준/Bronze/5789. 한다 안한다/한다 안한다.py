n = int(input())

for _ in range(n):
    s = input()
    l = len(s)//2
    if s[l] == s[l-1]:
        print('Do-it')
    else:
        print('Do-it-Not')