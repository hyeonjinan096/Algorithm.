function solution(progresses, speeds) {
    var answer = [];
    let list =[];
    let k;
    for(let i in progresses){
        
        k = ((100-progresses[i])/speeds[i]);
        if(parseInt(k)!=k){k = parseInt(k)+1;}
        list.push(k);
    }
    //console.log(list);
    let min = list[0];
    let sum =0;
    for(let i of list){
        if(min<i){answer.push(sum);sum =0;min= i;}
        sum++;
    }
    answer.push(sum);
    return answer;
}
//console.log(solution(	[95, 90, 99, 99, 80, 99,80], [1, 1, 1, 1, 1, 1,1]));