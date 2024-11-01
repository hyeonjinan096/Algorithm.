const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split('\n')

const N = Number(input.shift())
const values = input.shift().trim().split(' ').map(Number)

const dp = Array(N).fill(1)

for (let i = 0;i<N;i++){
    for (let j = 0;j<i;j++){
        if (values[i] > values[j]){
            dp[i] = Math.max(dp[i],dp[j]+1)
        }
    }
}

const answer = []
let order = Math.max(...dp)
for (let i = N-1;i>-1;i--){
    if (dp[i] === order){
        answer.push(values[i])        
        order--
    }
}

console.log(answer.length)
console.log(...answer.reverse())
