const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//5.37
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const n = Number(input.shift());

console.log(n % 2 !== 0 ? "SK" : "CY");
