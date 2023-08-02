function solution(order) {
    var answer = 0;
    let q = [];
    let n =0;
    let li = order.map((a)=>{n++; return n;})
    let j =0;
    
    for(let i of order){
        
        if(i == q[q.length-1]){ q.pop(); answer++; continue;}
        while(li[j]<i){
            q.push(li[j]);j++;
        }
        if(li[j] == i){li[j]; j++; answer++;}
        else{return answer;}
        
    }
    return answer;
}
//at[-1]알아보기
//시간초과