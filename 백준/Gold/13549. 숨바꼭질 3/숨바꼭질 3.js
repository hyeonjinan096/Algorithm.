const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split(' ').map(Number)

const [a,b] = input
const dp = Array(100001).fill(Infinity)

//bfs 완탐하는 배열 만들기 
function bfs(a){
    let q = [a]
    dp[a] = 0
    while(q.length){
        let cx = q.shift()
        if (cx+1>=0 && cx+1<100001 && dp[cx+1] > dp[cx]+1) {
            dp[cx+1] = dp[cx]+1
            q.push(cx+1)
        }
        if (cx-1>=0 && cx-1<100001 && dp[cx-1] > dp[cx]+1) {
            dp[cx-1] = dp[cx]+1
            q.push(cx-1)
        } 
        if (cx*2>=0 && cx*2<100001 && dp[cx*2] > dp[cx]) {
            dp[cx*2] = dp[cx]
            q.push(cx*2)
        }
    }
}

bfs(a)
console.log(dp[b])

