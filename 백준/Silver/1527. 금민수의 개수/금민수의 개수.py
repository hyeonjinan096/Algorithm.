from itertools import product
import sys

a,b = map(int,sys.stdin.readline().split())
x = len(str(a))
y = len(str(b))

count =0

for i in range(x, y+1):
    num_list = list(product([4,7],repeat=i))
    for num in num_list:
        number = int("".join(map(str,num)))
        if a<= number<=b:
            count+=1

print(count)