function solution(s) {
    var answer = 0;
    let arr =s+s;
    let k ;

    function check(a){
        let stack=[];
        for(let i of a){
            if(i == '[' ||i =='('||i =='{'){stack.push(i);}
            else{
                k = stack.pop();
                if(i ==']' &&k!='['){return false; }
                else if(i ==')'&&k!='('){return false;}
                else if(i =='}'&&k!='{'){return false;}
            }
        }
        if(stack.length!=0){return false;}
        else{return true;}
    }
    
    for(let i in s){
        let new_s = arr.substr(i,s.length);
        if(check(new_s)){answer++;}
    }
    
    return answer;
}