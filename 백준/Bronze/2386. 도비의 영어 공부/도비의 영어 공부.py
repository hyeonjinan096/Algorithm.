while True:
    list = input().split()
    l = list[0]
    answer = 0
    
    if l == '#':
        break
    s = ''.join(list[1:])
    for i in s:
        if l == i.lower():
            answer += 1
    print(l, answer)