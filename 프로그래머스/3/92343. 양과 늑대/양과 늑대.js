function solution(info, edges) {
    var answer = 0;
    let N = info.length
    let graph = [...Array(N)].map(()=>[])
    let visited = new Array(N).fill(0)
 
    //그래프 만들기 
    for (let [x,y] of edges){
        graph[x].push(y)
    }

    //0 양 1 늑대
    
    function dfs(sheep, wolf){
        if (sheep <= wolf) return
        
        answer = Math.max(sheep, answer)
        
        for (let [x,y] of edges){
            if (visited[x] && !visited[y]){
                visited[y] = 1
                if (info[y] === 0) dfs(sheep+1, wolf)
                else dfs(sheep, wolf+1)
                visited[y] = 0
            }
        }
    }
    
    visited[0] = 1
    dfs(1, 0)

    return answer;
}

//양 수 <= 늑대 수  양 먹힘
//최대한 많은 양 모아서 돌아오자
//한 번 방문한 노드의 길은 트인다. 주의

//방법1
//dfs를 쓰는데 가능한 다음 영역이 possible로 유기적으로 변경되는 거임
//방법2
//dfs를 쓰는데 앞에 방문했고 뒤에 방문 안한거 

//방법2로 한번 풀어보겠습니다. 
