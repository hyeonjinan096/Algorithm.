function solution(numbers, target) {
    var answer = 0;
    let arr = [];
    
    function dfs(k,i){
        if(i == numbers.length){
            if(k == target){answer++;}
            return;
        }
        dfs(k-numbers[i],i+1);
        dfs(k+numbers[i],i+1);
    }
    dfs(0,0);
    return answer;
}