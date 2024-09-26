from math import ceil
def solution(fees, records):
    answer=[]
    parking = {}
    result = {}
    [ b_t, b_p, p_t, p_p]= fees
    
    for record in records:
        time, car, io = record.split()
        h, m = map(int,time.split(":"))
        t = h*60 + m
        
        if io == 'IN':
            parking[car] = t
        else:
            if car not in result:
                result[car] = t-parking[car]
            else:
                result[car]+= t-parking[car]
            del parking[car]
    
    for car, t in parking.items():
        if car not in result:
            result[car] = (23*60+59) - t
        else:
            result[car] += (23*60+59) - t
            
    result = sorted(result.items(), key=lambda x:x[0])
    for car, t in result:
        print(car, t)
        answer.append(b_p + ceil(max(0,(t-b_t))/p_t)*p_p)
        
    return answer

#records -> time car io -> (time -> h,m -> t) 1,000
#io: i -> parking 데이터
#io: o -> time - car의 paking 데이터  #result 담기 /없으면 갱신, 있으면 추가 1,000
#parking -> last_time - parking데이터 
 
# result 차 번호 작은 거 부터 정렬 