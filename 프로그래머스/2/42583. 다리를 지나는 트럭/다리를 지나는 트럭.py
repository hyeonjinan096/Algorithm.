from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    cur_weight = 0 #sum의 시간복잡도 10000의 경우 위험
    
    while(bridge):
        cur_weight -= bridge.popleft()
        answer+=1
        if(truck_weights):
            if(cur_weight + truck_weights[0] <= weight):
                cur_weight+=truck_weights[0]
                bridge.append(truck_weights.popleft())
            else: 
                bridge.append(0)
    
    return answer