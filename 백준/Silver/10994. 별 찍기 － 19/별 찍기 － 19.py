import sys
n = int(sys.stdin.readline())

def func(c,n):
    if(n==1):
        s[c][c]='*'
        return 
    for i in range(c,4*n-3+c): 
        s[c][i]='*'
        s[4*n-4+c][i]='*'
        s[i][c]='*'
        s[i][4*n-4+c]='*'        
    func(c+2,n-1)


s= [[' ']*(4*n-3) for _ in range(4*n-3) ]

func(0,n)

for i in range(4*n-3):
    for j in range(4*n-3):
        print(s[i][j],end="")
    print()