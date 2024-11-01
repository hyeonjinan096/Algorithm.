const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split('\n')

const N = Number(input.shift())
const values = input.shift().trim().split(' ').map(Number)
const M = Number(input.shift())

let start = 0
let end = Math.max(...values)

while(start <= end){
    let mid = Math.floor((start + end)/2)
    let result = 0
    for (let value of values){
        if (value <= mid){result+=value}
        else {result+=mid}
    }
    if (result > M){
        end = mid-1
    } else {
        start = mid+1
    }
}

console.log(end)