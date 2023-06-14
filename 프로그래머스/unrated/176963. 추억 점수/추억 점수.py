def solution(name, yearning, photo):
    d = {name:score for name,score in zip(name,yearning)}
    answer=[]
    print(d)
    for i in photo:
        sum =0
        for j in i:
            if j in d:
                sum+=d[j]
        answer.append(sum)     
    return answer