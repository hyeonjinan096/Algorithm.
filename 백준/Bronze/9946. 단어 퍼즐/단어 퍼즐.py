N=1
while 1:
    a=input()
    b=input()
    if a=='END' and b=='END' :break
        
    na = [0]*26
    nb =[0]*26
    for i in a: na[ord(i)-97]+=1
    for i in b: nb[ord(i) - 97] += 1
        
    if na==nb: print("Case %d: same"%N)
    else: print("Case %d: different"%N)
    N+=1

