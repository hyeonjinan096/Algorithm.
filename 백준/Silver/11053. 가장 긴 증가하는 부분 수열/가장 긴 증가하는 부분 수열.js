const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split('\n')

const N = Number(input.shift())
const values = input[0].trim().split(' ').map(Number)

const dp = new Array(N).fill(1)

for(let i=0;i<N;i++){
    for(let j=0;j<i;j++){
        if (values[i] > values[j]){
            dp[i] = Math.max(dp[i],dp[j]+1)
        }
    }
}

console.log(Math.max(...dp))