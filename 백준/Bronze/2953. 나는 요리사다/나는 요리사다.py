answer = 0
idx = 0
for i in range(5):
    new = sum(list(map(int,input().split())))
    if answer < new:
        answer = new
        idx = i+1
print(idx,answer)