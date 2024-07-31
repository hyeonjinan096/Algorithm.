const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let [a, b] = input
  .shift()
  .split(" ")
  .map(e => Number(e));
let a_lst = input
  .shift()
  .split(" ")
  .map(e => Number(e));
let b_lst = input[0]
  .split(" ")
  .map(e => Number(e))
  .sort((a, b) => a - b);

const include = (v, arr) => {
  let start = 0;
  let end = arr.length - 1;
  let m = 0;

  while (start <= end) {
    m = Math.floor((start + end) / 2);
    if (arr[m] === v) {
      return true;
    } else if (arr[m] < v) {
      start = m + 1;
    } else {
      end = m - 1;
    }
  }
  return false;
};

let answer = new Array();

for (let i = 0; i < a_lst.length; i++) {
  if (!include(a_lst[i], b_lst)) {
    answer.push(a_lst[i]);
  }
}
console.log(answer.length);
if (answer.length) {
  answer.sort((a, b) => a - b);
  console.log(...answer);
}
