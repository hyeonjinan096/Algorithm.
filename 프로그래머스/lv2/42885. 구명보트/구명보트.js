function solution(people, limit) {
    //let visited= Array(people.length).fill(0);
    people.sort((a,b)=>b-a);
    let length = people.length;
    let count =0;
    
    for(let i in people){
        if(people.at(-1) + people[i]<= limit){
            people.pop();
        }
        count++;
    }
    return count;
}