function solution(k, dungeons) {
    var answer = 0;
    let d = dungeons;
    let visited = new Array(dungeons.length).fill(0);
    let c = 0;
    
    function dfs(K,c){
        answer = answer < c ? c : answer;
        for(let i in d){
            if(visited[i]==0 && K >= d[i][0]){
                visited[i] =1;
                dfs(K-d[i][1],c+1);
                visited[i] =0;
            }
        }
        return;
    }
  
    
    dfs(k,0);
   
    return  answer;
}
