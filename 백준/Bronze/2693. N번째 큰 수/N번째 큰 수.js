const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const iter = input[0];

let ans = [];

for (let i = 1; i <= iter; i++) {
  const arr = input[i]
    .split(" ")
    .map(Number)
    .sort((a, b) => b - a);

  ans.push(arr[2]);
}

console.log(ans.join("\n"));