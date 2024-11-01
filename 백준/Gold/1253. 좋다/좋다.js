const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split('\n')
const N = Number(input.shift())
const values = input[0].trim().split(' ').map(Number)
let answer = 0

values.sort((a,b)=>a-b)

for (let [idx, value] of values.entries()){
    let lst = [...values]
    lst.splice(idx,1)

    let start = 0
    let end = lst.length-1
    while(start<end){
        if (lst[start] + lst[end] === value) {
            answer++
            break
        } else if (lst[start] + lst[end] < value){
            start++
        } else {
            end--
        }
    }
}

console.log(answer)