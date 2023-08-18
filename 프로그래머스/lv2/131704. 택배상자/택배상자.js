function solution(order) {
    var answer = 0;
    let box = [];
    let box2 =[];
    let idx =0;
    for(let i in order){
        box.push(Number(i)+1);
    }
    let a;
    for(let i of order){
        if(box2.at(-1) == i ){
            answer++;
            box2.pop();
            continue;
        }
        while(box[idx]<i){
            box2.push(box[idx]);
            idx++;
        }
        if(box[idx] == i){idx++; answer++;}
        else{return answer;}
    }
    return answer;
}