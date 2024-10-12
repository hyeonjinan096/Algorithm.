from itertools import product
def solution(users, emoticons):
    answer = [0,0]
    data = [10,20,30,40]
    discount = []
    discount = list(product(data,repeat=len(emoticons)))
    
    for disc in discount:
        result = [0,0]
        for d, limit in users:
            pay = 0
            for j in range(len(disc)):
                if d<=disc[j]:
                    pay += emoticons[j] * (100 - disc[j])/100
                if pay >= limit:
                    break
            if pay >= limit:
                pay = 0
                result[0] +=1
            result[1] += pay
        answer = max(answer, result)

    return answer