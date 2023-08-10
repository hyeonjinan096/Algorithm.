function solution(s) {
    var answer = 0;
    let q =[];
    let S = s+s;
    let l = s.length;
    function check(s) {
        for(let i of s){
            if(i =="("||i=="["||i=="{"){
                if(i == "("){q.push(')');}
                else if(i == "["){q.push("]");}
                else if(i == "{"){q.push("}");}
            }
            else if(q.pop() != i ){
                return false
            }
        }
        if(q.length!=0){//q에 뭐가 있다
            return false
        }
        else{console.log("a");return true;}
    }
    
    for(let i in s){
        
        check(S.substr(i,l)) ? answer++ : 0;
       
    }
    
    
    
    return answer;
}