function solution(priorities, location) {
    var answer = 0;
    let q1 = [...priorities];
    let q2 = [];
    for(let i in priorities){
        q2.push(i);
    }
    let p;
    let l;
    let c=0;
    while(q1){
        p = q1.shift();
        l = q2.shift();
        if(Math.max(...q1)>p){
            q1.push(p);
            q2.push(l);
        }
        else{
            c++;
            if(l == location){
                return c;
            }
        }
    }
    
    return c;
}