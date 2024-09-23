from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights) 
    
    currentWeight = 0
    while bridge: 
        answer +=1
        
        currentWeight-=bridge.popleft()
        
        if truck_weights: 
            if currentWeight + truck_weights[0] <= weight:
                
                currentWeight += truck_weights[0]
                t = truck_weights.popleft()
                bridge.append(t)
            else:
                bridge.append(0)
    return answer
