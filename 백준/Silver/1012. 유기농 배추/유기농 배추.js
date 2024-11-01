const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split('\n')

const T = Number(input.shift().trim())

const dir = [[1,0],[-1,0],[0,1],[0,-1]]

for (let i = 0;i<T;i++){
    let answer = 0
    const [N,M,K] = input.shift().trim().split(' ').map(Number)
    const graph = [...Array(N)].map(()=>Array(M).fill(0))
    for (let j =0;j<K;j++){
        const [x,y] = input.shift().trim().split(' ').map(Number)
        graph[x][y] = 1
    }


    //bfs로 탐색하면서 연결되어있는 1인 곳만 방문하고 방문 처리 2
    function bfs(x,y){
        const q = [[x,y]]
        graph[x][y] = 2
        while(q.length){
            const [cx,cy] = q.shift()
            for (let [dx, dy] of dir){
                let nx = cx+ dx
                let ny = cy+ dy

                if (nx>=0 && nx<N && ny>=0 && ny<M && graph[nx][ny] ===1){
                    graph[nx][ny] = 2
                    q.push([nx,ny])
                }
            }
        }
    }

    function dfs(x,y){
        graph[x][y] = 2
        for (let [dx,dy] of dir){
            let nx = x+dx
            let ny = y+dy
            if (nx>=0 && nx<N && ny>=0 && ny<M && graph[nx][ny] ===1){
                dfs(nx,ny)
            }
        }
    }

    //for문 돌면서 1인 공 방문하고 거기서 퍼지는 거 확인하기 위해 bfs 돌리기
    for (let i=0;i<N;i++){
        for (let j =0;j<M;j++){
            if (graph[i][j] === 1){
                dfs(i,j)
                answer++
            }
        }
    }

    console.log(answer)
}
