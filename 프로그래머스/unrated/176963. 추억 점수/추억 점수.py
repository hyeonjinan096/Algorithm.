def solution(name, yearning, photo):
    score = {n : s for n,s in zip(name,yearning)}
    answer = []
    for i in photo:
        sum =0
        for j in i:
            if j in score.keys():  #이걸 빼먹음 .key하면 key값도 따질 수 있음
                sum +=score[j]
        print(sum)
        answer.append(sum)
    
    return answer