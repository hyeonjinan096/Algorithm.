function solution(stones, k) {
    let start = 1
    let end = 200000000

    while(start<=end){
        let mid = Math.ceil((start + end)/2)
        let cnt = 0
        for(let stone of stones){
            if (stone-mid <= 0){ 
                cnt++
            }else cnt = 0
            
            if(cnt >= k){
                end = mid-1
                break
            }
        } 
        if(cnt < k){
            start = mid+1
        }
    }
    return start;
}