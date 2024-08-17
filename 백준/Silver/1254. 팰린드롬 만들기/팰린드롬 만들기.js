const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//12.17
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let str = input[0].split("");

//가운데 부터 끝까지
let mid = Math.floor(str.length / 2);
let lst = [];
for (let i = mid; i < str.length; i++) {
  for (let j = 0; j <= str.length - mid; j++) {
    let x = i - j;
    let y = i + j;
    if (x < 0 || y >= str.length) {
      lst.push(x + 1);
    }
    if (str[x] !== str[y]) {
      break;
    }
  }
}

for (let i = mid; i < str.length; i++) {
  for (let j = 1; j <= str.length - mid; j++) {
    let x = i - j;
    let y = i + j - 1;
    if (x === 0 && y === str.length - 1 && str[x] === str[y]) {
      lst.push(0);
    }
    if (x < 0) {
      lst.push(y);
    }
    if (y > str.length - 1) {
      lst.push(x + 1);
    }
    if (str[x] !== str[y]) {
      break;
    }
  }
}
console.log(str.length + Math.min(...lst));
