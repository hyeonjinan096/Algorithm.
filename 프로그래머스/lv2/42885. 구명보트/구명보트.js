function solution(people, limit) {
    var answer = 0;
    people.sort((a,b)=>b-a);
    for(let i of people){
        if(i + people.at(-1)<=limit){
            people.pop();
        }
        answer++;
    }
    
    
    return answer;
}