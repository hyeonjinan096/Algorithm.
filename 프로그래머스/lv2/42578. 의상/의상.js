function solution(clothes) {
    var answer = 0;
    let object = {};
    
    for(let i of clothes){
        object[i[1]] = (object[i[1]]||0)+1;
    }
    let sum=1;
    for(let i in object){
        sum *=(object[i]+1)
    }
    
    return sum-1;
}