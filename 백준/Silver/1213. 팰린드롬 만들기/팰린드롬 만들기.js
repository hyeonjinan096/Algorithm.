const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//6.53
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const values = input[0].split("");

const getPalindrome = values => {
  let words = {};
  for (let i of values) {
    i in words ? (words[i] += 1) : (words[i] = 1);
  }

  let mid = "";
  let side = [];
  for (let key in words) {
    if (words[key] % 2 !== 0) {
      if (mid) {
        return "I'm Sorry Hansoo";
      }
      mid = key;
      words[key] -= 1;
    }
    for (let i = 0; i < words[key] / 2; i++) {
      side.push(key);
    }
  }

  side.sort((a, b) => (a > b ? 1 : -1));
  return side.join("") + mid + side.reverse().join("");
};

console.log(getPalindrome(values));
