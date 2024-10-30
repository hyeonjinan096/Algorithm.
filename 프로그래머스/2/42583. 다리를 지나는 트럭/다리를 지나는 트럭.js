function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let bridge = new Array(bridge_length).fill(0)
    let bridge_weight = 0 
    
    let idx = 0
    while(bridge.length){
        answer++
        bridge_weight -= bridge.shift()
        
        if (idx < truck_weights.length){
            if (truck_weights[idx] + bridge_weight <=weight){
                bridge.push(truck_weights[idx])
                bridge_weight+=truck_weights[idx]
                idx++
            }
            else bridge.push(0)
        }
        
    }
    
    
    
    return answer;
}