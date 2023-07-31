function solution(numbers, target) {
    var answer = 0;
    
    function dfs(N,result,p){
        result = result +numbers[N]*p
        if(N == numbers.length-1){
            if(result ==target){answer++;}
            return;}
        dfs(N+1,result,1);
        dfs(N+1,result,-1);
        
        
    }
    dfs(0,0,1);
    dfs(0,0,-1);
    
    return answer;
}