function solution(clothes) {
    var answer = 1;
    let object ={};
    for(let i of clothes){
        object[i[1]] = (object[i[1]]||0)+1;
    }
    for(let i in object){
        answer*=(object[i]+1);
    }
    return answer-1;
}