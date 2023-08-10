function solution(s) {
    var answer = '';
    let S = s.split(" ")
    return Math.min(...S)+" "+Math.max(...S);    
}