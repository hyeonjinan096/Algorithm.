function solution(s) {
    var answer = '';
    let flag = 0;
    for(let i of s){
        if(i==' '){flag =0;answer+=i;}
        else if(flag == 0 ){
            answer+=i.toUpperCase();
            flag = 1;
        } 
        else if(flag ==1){
            answer+=i.toLowerCase();
        }
        
    }
    return answer;
}