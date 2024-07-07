//dfs함수

function solution(maps) {
    var answer = [];
    let result =[];
    const [R,C] = [maps.length, maps[0].length]
    const visited = Array.from({length: R},()=>Array(C).fill(0)) //문법 확인
    const dir = [[0,1],[0,-1],[1,0],[-1,0]]
    
    const bfs = (a,b) => {
        let cnt = 0;
        const q = [[a,b]];
        cnt+=parseInt(maps[a][b])
        visited[a][b] = 1;
        while (q.length) {
            const [x,y] = q.shift();
            for (let i =0;i<4;i++){
                const nx = x + dir[i][0];
                const ny = y + dir[i][1];
                if (nx >= 0 && ny >= 0 && nx<R && ny <C){
                    if(!visited[nx][ny] && maps[nx][ny] !=='X') {
                        visited[nx][ny]=1;
                        cnt+=parseInt(maps[nx][ny])
                        q.push([nx,ny])
                    }
                }
            }
        };
        result.push(cnt)
    }
    
    //섬이면 bfs로 넘기기
    for (let i =0;i<R;i++) {
        for (let j=0;j<C;j++){
            if( !visited[i][j] && maps[i][j] !== "X") bfs(i,j);
        }
    }
    
    if(result.length === 0) return [-1]
    
    return result.sort((a,b) => a-b);
}

//dfs에서 필요한 재료 
//visited