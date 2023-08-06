N, K = map(int, input().split(' '))
li = list(map(int, input().split(',')))
temp = []


for i in range(K):
    for j in range(len(li) - 1):
        temp.append(li[j + 1] - li[j])

  
    li = temp

    temp = []

print(','.join(list(map(str, li))))