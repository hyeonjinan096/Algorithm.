function solution(number, k) {
    var answer = '';
    num_lst=Array.from(number).map(Number)
    answer = []

    for(let num of num_lst){
        if (answer.length === 0){
            answer.push(num)
            continue
        }
        while (k>0 && answer[answer.length-1] < num){
            answer.pop()
            k--
        } 
        answer.push(num)
        
    }
    
    while(k>0){
        answer.pop()
        k--
    }
    
    return answer.join('');
}

console.log(solution("22",1))