n,m,t = map(int,input().split())

mx = max(n,m)
mn = min(n,m)


cnt = 0

b = 0
c = 100000

while(t>=mx*cnt):
    tmp_t = t-cnt*mx
    tmp_b = cnt + tmp_t//mn
    tmp_c = tmp_t % mn
    if(c>tmp_c):
        b = tmp_b
        c = tmp_c
    elif(c == tmp_c and tmp_b>b):
        b = tmp_b
        c = tmp_c
    cnt+=1
print(f'{b} {c}')
