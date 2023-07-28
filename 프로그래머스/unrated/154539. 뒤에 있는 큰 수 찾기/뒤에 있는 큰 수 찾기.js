function solution(numbers) {
    let answer = Array(numbers.length).fill(-1);
    let stack = [];
    
    for(let i in numbers){
        while(numbers[stack.at(-1)]<numbers[i]){
            answer[stack.pop()] =numbers[i];
        }
        stack.push(i);
    }
    
    return answer;
}