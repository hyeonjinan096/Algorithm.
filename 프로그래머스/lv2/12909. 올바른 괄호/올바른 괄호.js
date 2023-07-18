//복습2
function solution(s){
    
    let stack =0;
    for(let i of s){
        i === "(" ? stack++ : stack--;
        if(stack<0){return false;}
    }
    if(stack != 0){return false;}
    else{return true;}
    
    
}