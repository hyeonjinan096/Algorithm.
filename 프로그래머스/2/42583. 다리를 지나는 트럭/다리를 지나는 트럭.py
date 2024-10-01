from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    bridge_weight =0
    truck = deque(truck_weights)
    while(bridge):
        bridge_weight -= bridge.popleft()
        answer +=1
        if(truck):
            if bridge_weight + truck[0] <= weight:
                bridge_weight += truck[0]
                bridge.append(truck.popleft())
            else:
                bridge.append(0)

    return answer