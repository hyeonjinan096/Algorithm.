function solution(priorities, location) {
    var answer = 0;
    let q1 = priorities;
    let q2 = [];
    let p;
    let l;
    let count =0;
    for(let i in q1){
        q2.push(i);
    }
    
    while(q1){
        p = q1.shift();
        l = q2.shift();
        if(Math.max(...q1)>p){
            q1.push(p);
            q2.push(l);
        }
        else{
            count++;
            if(l == location){
                return count;
            }
        }
    }
    return answer;
}