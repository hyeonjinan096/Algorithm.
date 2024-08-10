const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//3.37
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let [n, m] = input
  .shift()
  .split(" ")
  .map(e => Number(e));

let graph = Array.from(Array(n + 1), () => []);

for (let i = 0; i < m; i++) {
  [a, b] = input
    .shift()
    .split(" ")
    .map(e => Number(e));

  graph[a].push(b);
  graph[b].push(a);
}

let visited = Array.from(Array(n + 1), () => -1);

const bfs = v => {
  q = [[v, 0]];
  visited[v] = 0;

  while (q.length) {
    let [cur, dis] = q.shift();
    for (let i of graph[cur]) {
      if (visited[i] === -1) {
        visited[i] = dis + 1;
        q.push([i, dis + 1]);
      }
    }
  }
};

bfs(1);

// console.log(visited);

const max_dis = Math.max(...visited);
let answer = [];

for (let i in visited) {
  if (visited[i] === max_dis) {
    answer.push(i);
  }
}

console.log(answer[0], max_dis, answer.length);
