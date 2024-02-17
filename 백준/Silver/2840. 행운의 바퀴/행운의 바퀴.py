n, k = map(int, input().split())
circle = ['?'] * n

for i in range(k):
    spin = input().split()
    m = int(spin[0]) % n
    s_char = str(spin[1])	
    circle = circle[-m:] + circle[:-m]	

    if circle[0] == '?':
        if s_char in circle:
            print('!')
            break
        circle[0] = s_char
    elif circle[0] == s_char:
        continue
    else:
        print('!')
        break
else:
    print("".join(circle))