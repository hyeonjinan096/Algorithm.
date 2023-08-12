function solution(numbers) {
    let N = numbers;
    var answer = new Array(N.length).fill(0);
    let q=[];
    for(let i in N){
        while(N[i] > N[q.at(-1)]){
            answer[q.at(-1)] = N[i];
            q.pop();
        }
        q.push(i);
    }
    answer = answer.map((e)=>{if(e==0){return -1;}else{return e}})
    
    return answer;
}