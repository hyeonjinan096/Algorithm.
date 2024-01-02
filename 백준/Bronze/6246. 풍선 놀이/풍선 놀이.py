
N, Q = map(int, input().split(' '))

v = [None for x in range(N)]


for i in range(Q):
    L, I = map(int, input().split(' '))
    for index in range(L-1, N, I):
        v[index] = 'balloon'

print(v.count(None))