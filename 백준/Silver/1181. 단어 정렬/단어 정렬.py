import sys
n = int(sys.stdin.readline())

a=[]
for i in range(n):
    s = str(sys.stdin.readline()) #개행문자까지 포함 #.strip()사용하면 개행 제거 가능
    a.append([int(len(s)),s])

a.sort()

for i in range(n):
    if(i==0 or a[i][1]!=a[i-1][1]):
        print(a[i][1],end="") #end=""없으면 개행 두번됨


