case = 1
while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    cnt = i = 0
    while (i+1)*i // 2 < a:
        i += 1
    while (i+1)*i // 2 < b-1:
        t = (i+1)*i // 2 + 1
        if t**0.5 == int(t**0.5):
            cnt += 1
        i += 1
    print(f"Case {case}: {cnt}")
    case += 1