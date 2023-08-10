function solution(s){
    var answer = true;
    let q =0;
    for(let i of s){
        if(i=="("){q++;}
        else{q--;}
        if(q<0){return false;}
    }
    if(q==0){return true;}
    else{return false;}
    return answer;
}