import sys
n = int( sys.stdin.readline())
s=[]
for i in range(n):
    a=int(sys.stdin.readline())
    if(a==0):
        s.pop(-1)
    else:
        s.append(a)


print(sum(s))