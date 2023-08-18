function solution(numbers, target) {
    var answer = 0;
    
    function dfs(i,n){
        if(i == numbers.length){
            if(n == target){answer++;}
            return;
        }
        dfs(i+1,n+numbers[i]);
        dfs(i+1,n-numbers[i])
        return;
    }
    
    dfs(0,0);
    return answer;
}