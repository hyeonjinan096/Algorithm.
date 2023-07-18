//복습2
function solution(s){
    
    let stack =0;
    for(let i of s){
        i === "(" ? stack++ : stack--;
        if(stack<0){return false;}
    }
    return stack ==0 ? true : false;
    
    //if(stack == 0){return true;}
    //else{return false;} 왜 true가 앞이면 시간초과인지 모르겠음;;
    
    
}