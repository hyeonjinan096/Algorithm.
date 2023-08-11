function solution(numbers) {
    var answer = 0;
    let flag =0;
    let visited = Array(numbers.length).fill(0);
    let set = new Set();
    function check(n){
        if(n == 1){return false;}
        for(let i=2;i<=Math.sqrt(n);i++){
            if(n%i==0){return false;}
        }
        return true;
    }//소수 판별 함수
    
    function dfs(k){
        set.add(parseInt(k));

        for(let i in numbers){
            if(visited[i]==0){
                visited[i] =1;
                dfs(k+numbers[i]);
                visited[i] =0;
            }
        }
    }
    
    for(let i in numbers){
        if(numbers[i] != '0'){
            visited[i] =1;
            dfs(numbers[i]);
            visited[i] =0;
        }
    }
    
    for(let i of set){
        if(check(i)){answer++;}
    }
    return answer;
}