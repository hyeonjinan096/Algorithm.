function solution(progresses, speeds) {
    var answer = [];
    let arr =progresses.map((e,i)=>Math.ceil((100-e)/speeds[i]));
    let m=0;
    let c=0;
    for(let i of arr){
        if(m==0){m = i;}
        else if(m<i){answer.push(c); c=0; m =i;}
        c++;
    }
    answer.push(c);
    return answer;
}