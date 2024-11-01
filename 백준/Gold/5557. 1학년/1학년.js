const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split('\n')

const N = Number(input.shift())
const values = input[0].trim().split(' ').map(Number)

const dp = [...Array(N-1)].map(()=>Array(21).fill(BigInt(0)))

dp[0][values[0]] = BigInt(1)

for (let [idx,value] of values.entries()){
    if (idx === 0 || idx === N-1) continue
    for (let [n,cnt] of dp[idx-1].entries()){
        if (cnt > 0){
            if (n+value>=0 && n+value <=20) dp[idx][n+value] += BigInt(cnt)
            if (n-value>=0 && n-value <=20) dp[idx][n-value] += BigInt(cnt)
        }
    }
    // console.log(idx,dp[idx])
}
console.log(dp[dp.length-1][values[N-1]].toString())