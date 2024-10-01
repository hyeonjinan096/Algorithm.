import math

def solution(fees, records):
    answer = []
    b_t, b_m, p_t,p_m = fees
    parking = {}
    result = {}
    last_time = 23*60 + 59
    for record in records:
        time, car, io = record.split()
        h,m = map(int,time.split(':'))
        t = h*60 + m
        
        if io == "IN":
            parking[car] = t
        else:
            if car not in result:
                result[car] = 0
            result[car] += t-parking[car]
            del parking[car]
    
    for car, t in parking.items():
        if car not in result:
            result[car] = 0
        result[car] += last_time-parking[car]
    
    result = sorted(result.items(), key = lambda x:x[0])
  
    answer = []
    for car, t in result:
        answer.append(b_m + (math.ceil(max(0,t-b_t)/p_t))*p_m)
        
    
    return answer