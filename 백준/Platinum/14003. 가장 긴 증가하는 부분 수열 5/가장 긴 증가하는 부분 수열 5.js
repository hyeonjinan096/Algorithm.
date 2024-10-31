const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split('\n')

const N = Number(input.shift())
const values = input[0].trim().split(' ').map(Number)
const result = []
const idx_result = []

function binarySearch(arr,value){
    let start = 0
    let end = arr.length-1
    while(start<=end){
        let mid = Math.floor((start + end)/2)
        if (arr[mid] >= value){
            end = mid-1
        } else {
            start = mid+1
        }
    }

    return start
}


for (let [i,value] of values.entries()){
    let idx = binarySearch(result,value)
    if (idx === result.length){
        result.push(value)
    }else {
        result[idx] = value
    }

    idx_result[i] = idx
}

let order = Math.max(...idx_result)
let answer = []
for (let i=N-1;i>-1;i--){
    if (idx_result[i] === order){
        answer.push(values[i])
        order--
    }
}

console.log(answer.length)
console.log(...answer.reverse())
