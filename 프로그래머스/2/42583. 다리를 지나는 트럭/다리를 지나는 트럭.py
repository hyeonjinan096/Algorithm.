from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    bride_weight = 0
        
    while bridge: 
        bride_weight-=bridge.popleft()
        answer+=1
        if truck_weights:
            if bride_weight + truck_weights[0] <= weight: #
                bride_weight+=truck_weights[0]
                bridge.append(truck_weights.popleft()) 
            else:
                bridge.append(0)
    
    return answer