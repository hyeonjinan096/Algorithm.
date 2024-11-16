from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    idx = 0
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    b_weight = 0
    l = len(truck_weights)
    
    while(bridge):
        answer+=1
        b_weight-=bridge.popleft()
        
        if truck and b_weight + truck[0] <= weight:
            t = truck.popleft()
            bridge.append(t)
            b_weight+=t 
        elif truck:
            bridge.append(0)
        
    
    
    return answer