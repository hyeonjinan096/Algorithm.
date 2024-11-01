const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split('\n')
const [N,M,X] = input.shift().trim().split(' ').map(Number)

const graph = [...Array(N+1)].map(()=>[])
const reverse_graph = [...Array(N+1)].map(()=>[])

for (let data of input){
    let [x,y,t]=data.trim().split(' ').map(Number)
    graph[x].push([y,t])
    reverse_graph[y].push([x,t])
}

function bfs(x,graph){
    let dp = new Array(N+1).fill(Infinity)
    let q = [x]
    dp[q] = 0

    while(q.length){
        let cx = q.shift()
        for (let [nx,nt] of graph[cx]){
            if (dp[nx] > dp[cx]+nt){
                dp[nx] = dp[cx]+nt
                q.push(nx)
            }
        }
    }
    
    return dp
}

let go = bfs(X,reverse_graph)
let back = bfs(X, graph)

let answer = 0
for (let i=1;i<=N;i++){
    answer = Math.max(go[i]+back[i],answer)
}

console.log(answer)