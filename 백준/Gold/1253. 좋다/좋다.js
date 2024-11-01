const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split('\n')
const N = Number(input.shift())
const values = input[0].trim().split(' ').map(Number)
let answer = 0
for (let [idx, value] of values.entries()){
    let lst = [...values]
    lst.splice(idx,1)

    for (let i = 0;i<N-1;i++){
        let flag = 0
        for (let j = i+1;j<N-1;j++){
            if (lst[i]+lst[j] === value) {
                flag =1
                break
            }
        }
        if (flag) {
            answer++
            break
        }
    }
}

console.log(answer)