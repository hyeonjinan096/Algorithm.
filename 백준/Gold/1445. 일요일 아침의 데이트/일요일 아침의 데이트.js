const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split('\n')
const [N,M] = input.shift().trim().split(' ').map(Number)
const graph = []
let flower = [0,0]
let start = [0,0]
const info = [...Array(N)].map(()=>Array(M).fill([Infinity,Infinity]))
const dir = [[0,1],[0,-1],[1,0],[-1,0]]

for (let data of input){
    graph.push(data.trim().split(''))
}

//꽃 위치와 시작점 찾기
for (let i = 0;i<N;i++){
    for (let j = 0;j<M;j++){
        if (graph[i][j] === 'F'){
            flower = [i,j]
        }else if (graph[i][j] === 'S'){
            start = [i,j]
        }
    }
}

//데이터 업데이트 하기
function updateData(x,y,g,ng){
    let [og, ong] = info[x][y]
    if (og > g || (og === g && ong>ng)){
        info[x][y] = [g,ng]
        q.push([x,y,g,ng])
    }
}

//옆에 쓰레기 있는지 확인하기
function hasNextGarbage(x,y){
    let result = false
    for (let [dx,dy] of dir){
        if (x+dx>=0 && x+dx <N && y+dy>=0 && y+dy<M){
            if (graph[x+dx][y+dy] === 'g'){
                result = true
                break
            }
        }
    }
    return result
}


let q = []
//bfs돌고 누적값 갱신하면서 최적합 구하기 
function bfs([x,y]){
    q = [[x,y,0,0]]
    info[x][y] = [0,0]
    while(q.length){
        [curx, cury, curg, curng] = q.shift()
        for (let [dx,dy] of dir){
            let nx = curx + dx
            let ny = cury + dy
            if (nx>=0 && nx <N && ny>=0 && ny<M){
                if (graph[nx][ny] === 'F'){
                    updateData(nx,ny,curg,curng)
                } else if(graph[nx][ny] === 'g'){
                    updateData(nx,ny,curg+1,curng)
                } else if(graph[nx][ny] === '.' && hasNextGarbage(nx,ny)){
                    updateData(nx,ny,curg,curng+1)
                } else {
                    updateData(nx,ny,curg,curng)
                }
            }
        }
    }
}

bfs(start)

console.log(...info[flower[0]][flower[1]])
