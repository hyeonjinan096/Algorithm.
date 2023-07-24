function solution(clothes) {
    var answer = 1;
    let c =[];
    let N;
    
    for (let i of clothes){
        if(!c[i[1]]){
            c[i[1]] =1;
        }
        else{
            c[i[1]] +=1;
        }
    }
    console.log(c);
 
    for(let i in c){ //object는 of 사용 안됨
        //console.log(i);
        answer *= (c[i]+1);       
    }
    return answer-1;
}