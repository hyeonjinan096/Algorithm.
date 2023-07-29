function solution(k, dungeons) {
    var answer = [];
    let visited =Array(dungeons.length).fill(0);
    
    function dfs(k,result){
        answer =answer<result? result : answer;
        for(let i in dungeons){
            if(visited[i]==0 && k >= dungeons[i][0]){
                visited[i] = 1;
                dfs(k-dungeons[i][1],result+1)
                visited[i] =0;
            }
            
        }
        return answer;
    }
    
    return (dfs(k,0));
}