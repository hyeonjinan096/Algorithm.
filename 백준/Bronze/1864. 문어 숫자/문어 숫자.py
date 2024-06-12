dic = {'-':0,'\\':1,'(':2,'@':3,'?':4,'>':5,'&':6,'%':7,'/':-1}
while(1):
    str = input()
    if str == '#':
        break
    answer = 0
    j = 0
    for i in range(len(str)-1,-1,-1):
        answer+=((8**i)*dic[str[j]])
        j+=1
    print(answer)