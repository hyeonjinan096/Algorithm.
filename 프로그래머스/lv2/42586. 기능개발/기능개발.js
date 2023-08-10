function solution(progresses, speeds) {
    var answer = [];
    let li =[];
    let day ;
    for(let i in speeds){
        day = (100-progresses[i])/speeds[i];
        if(parseInt(day) != day){day = parseInt(day)+1;}
        li.push(day); 
    }
    console.log(li);
    let min =li[0];
    let sum =0;
    for(let i of li){
        if(min<i){answer.push(sum);sum =0;min =i;}
        sum++;
    }
    answer.push(sum);
    return answer;
}