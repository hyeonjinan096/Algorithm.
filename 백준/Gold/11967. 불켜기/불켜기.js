const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split('\n')

const [N,M] = input.shift().trim().split(' ').map(Number)

const graph = [...Array(N)].map(()=>[...Array(N)].map(()=>[]))
const visited = [...Array(N)].map(()=>Array(N).fill(0))
//0-> 방문X 불켜짐X
//1-> 방문X 불켜짐o
//2-> 방문o 불켜짐o

let answer = 0
const dir = [[1,0],[-1,0],[0,1],[0,-1]]

for (let data of input){
    let [x,y,a,b]= data.trim().split(' ').map(Number)
    graph[x-1][y-1].push([a-1,b-1])
}

function isOk(x,y) {
    if (x>=0 && x<N && y>=0 && y<N){
        return true
    }
    return false
}

let q = []

function switchLight(x,y){
    for (let [nx,ny] of graph[x][y]){
        if (visited[nx][ny] === 0){
            visited[nx][ny] = 1// 불키기
            answer++
            //접근 가능한지 확인하기 
            for (let [dx, dy] of dir){
                if (isOk(nx+dx,ny+dy) && visited[nx+dx][ny+dy] === 2){
                    visited[nx][ny] = 2
                    q.push([nx,ny])
                    break
                }
            }
        }
    }
}

function bfs(){
    q = [[0,0]]
    visited[0][0] = 2
    answer++

    while(q.length){
        const [cx,cy]= q.shift()
        switchLight(cx,cy)
        
        for (let [dx,dy] of dir){
            let nx = cx + dx
            let ny = cy + dy
            if (isOk(nx, ny) && visited[nx][ny] === 1){
                visited[nx][ny] = 2
                q.push([nx,ny])
            }
        }
    }
}

bfs()

console.log(answer)
