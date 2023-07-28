//경로탐색#네트워크#조합만들기🌰
//dfs🌰#bfs
//visited
//재귀함수
function solution(k, dungeons) {
    let d = dungeons;
    let visited = Array(d.length).fill(0) //1.visited만들기
    let answer = 0;
    function dfs(k,result){
        answer = answer <result ? result: answer;
        
        for(let i in d){
            if(k>=d[i][0] && visited[i] ==0 ){
                visited[i] =1;
                dfs(k-d[i][1],result+1);
                visited[i] =0;
            }
        }
        
        return answer;
    }
    
    
    
    return dfs(k, 0);
}