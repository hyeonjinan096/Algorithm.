const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split('\n')

const N = Number(input.shift())
const values = input.shift().trim().split(' ').map(Number)
const result = []
const idx_result = Array(N).fill(0)

//이중탐색 
function binarySearch(arr,value){
    let start = 0
    let end = arr.length-1
    while(start<=end){
        let mid = Math.floor((start+end)/2)
        if (arr[mid]>=value){
            end = mid-1
        } else {
            start = mid+1
        }
    }
    return start
}


//values 탐색
for (let [idx,value] of values.entries()){
    const index = binarySearch(result, value)
    if (index === result.length){
        result.push(value)
    } else {
        result[index] = value
    }
    idx_result[idx] = index
}

const answer = []
let order = Math.max(...idx_result)

for (let i = N-1;i>-1;i--){
    if (idx_result[i] === order){
        answer.push(values[i])
        order--
    }
}

console.log(answer.length)
console.log(...answer.reverse())