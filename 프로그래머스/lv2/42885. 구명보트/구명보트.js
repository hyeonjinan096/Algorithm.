function solution(people, limit) {
    
    people.sort((a,b)=>b-a);
    let count =0;
    
    for(let i in people){
        if(people.at(-1) + people[i]<= limit){
            people.pop();
        }
        count++;
    }
    return count;
}