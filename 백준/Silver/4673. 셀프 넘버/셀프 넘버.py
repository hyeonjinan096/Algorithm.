def d(n):
    n = n + sum( map(int, str(n)) )
    return n

nonSelf = set()

for i in range(1, 10001):
    nonSelf.add( d(i) )

for j in range(1, 10001):
    if j not in nonSelf:
        print(j)
        
