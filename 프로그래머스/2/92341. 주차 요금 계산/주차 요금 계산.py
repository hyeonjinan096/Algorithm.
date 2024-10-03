import math
def solution(fees, records):
    answer = []
    b_t, b_f, p_t,p_f = fees
    parking = {}
    result = {}
    last_time = 23*60+59
    
    for record in records:
        t, car, io = record.split()
        h,m = map(int,t.split(':'))
        time = h*60+m
        if io == 'IN':
            parking[car] = time
        else:
            if car in result:
                result[car] += time-parking[car]
            else:
                result[car] = time-parking[car]
            del parking[car]
        
    for car, time in parking.items():
        if car in result:
            result[car] += last_time-parking[car]
        else:
            result[car] = last_time-parking[car]
            
    result = sorted(result.items(), key=lambda x:x[0])
   
    answer = []
    for car,time in result:
        answer.append(b_f + math.ceil(max(0,time-b_t)/p_t)*p_f)
    
    return answer