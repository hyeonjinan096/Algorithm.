const fs = require('fs')
const input = fs.readFileSync('/dev/stdin','utf8').trim().split(' ').map(Number)
console.log(input[0] + input[1])