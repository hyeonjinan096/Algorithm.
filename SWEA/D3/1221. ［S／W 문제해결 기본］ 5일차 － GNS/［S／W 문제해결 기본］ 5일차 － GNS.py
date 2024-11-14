dic = {
    "ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5,
     "SIX":6, "SVN":7, "EGT":8, "NIN":9
}

T = int(input())

for test_case in range(1, T + 1):
    N,L = map(str,input().split())
    L = int(L)
    values = input().split()
    values.sort(key = lambda x:dic[x])
    
    print(f'#{test_case} ',end = '')
    print(*values)