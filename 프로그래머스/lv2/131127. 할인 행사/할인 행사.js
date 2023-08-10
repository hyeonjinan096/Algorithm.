function solution(want, number, discount) {
    var answer = 0;
    let day = number.reduce((s,c)=>s+c,0)
    let li;
    let N  = number;
    for(let i=0;i<discount.length;i++){
        li = discount.slice(i,i+day);
        N  = number.map((e)=>e);
        for(let j =0;j<want.length;j++){
            while(li.includes(want[j])){
                li[li.indexOf(want[j])] = "";
                N[j]--;
            }
        }
        N.sort((a,b)=>b-a);
        if(N[0]<=0){
            answer++;
        }
    
    }
    
    return answer;
}