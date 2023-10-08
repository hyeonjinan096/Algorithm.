N = [-1]*9

for i in range(9):
    N[i] = int(input())
    
N = sorted(N)
for i in range(8):
    for j in range(i+1, 9):
        if sum(N) - (N[i]+N[j]) == 100:
            a = N[i]
            b = N[j]

N.remove(a)
N.remove(b)
for i in N:
    print(i)