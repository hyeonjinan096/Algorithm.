const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split('\n')

const N = Number(input.shift())
const values = input[0].trim().split(' ').map(Number)
const result = []

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


for (let value of values){
    let idx = binarySearch(result,value)
    if (idx === result.length){
        result.push(value)
    }else {
        result[idx] = value
    }
}

console.log(result.length)