from math import ceil

def solution(fees, records):
    answer = []
    b_time, b_pay, p_time, p_pay = fees
    parkings = {}
    results = {}
    last_time = 23*60+59
    
    for record in records:
        time, car, io = record.split()
        h, m = map(int,time.split(':'))
        t = h* 60 + m
        
        if io == 'IN':
            parkings[car] = t
        else:
            if car in results:
                results[car] += t-parkings[car]
            else:
                results[car] = t-parkings[car]
            del parkings[car] #확인하기
            
    for car, t in parkings.items():
        if car in results:
            results[car] += last_time - t
        else:
            results[car] = last_time - t
    
    results = sorted(results.items(), key=lambda  x:x[0])
    
    for car, t in results:
        answer.append(b_pay + max(0,ceil((t-b_time)/p_time))*p_pay)

    return answer