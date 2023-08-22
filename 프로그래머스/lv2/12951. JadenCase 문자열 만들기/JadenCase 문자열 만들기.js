function solution(s) {
    var answer = '';
    let flag =0;
    for(let i of s){
        if(flag ==0){
            i= i.toUpperCase();
            flag =1;
        }
        else if(flag ==1 &&i.toUpperCase()==i){
            i = i.toLowerCase();
        }
        if(i ==' '){flag =0;}
        answer +=i;
    }
    return answer;
}