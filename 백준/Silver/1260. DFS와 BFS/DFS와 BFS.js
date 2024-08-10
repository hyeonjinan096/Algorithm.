const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//2.14
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m, v] = input
  .shift()
  .split(" ")
  .map(e => Number(e));

graph = Array.from(Array(n + 1), () => []);
for (let i = 0; i < m; i++) {
  const [a, b] = input
    .shift()
    .split(" ")
    .map(e => Number(e));
  graph[a].push(b);
  graph[b].push(a);
}
graph.map(e => e.sort((a, b) => a - b));

let dfs_result = [];
const dfs = v => {
  dfs_result.push(v);
  for (let i of graph[v]) {
    if (!dfs_result.includes(i)) {
      dfs(i);
    }
  }
};

let bfs_result = [];
const bfs = v => {
  q = [v];
  bfs_result.push(v);
  while (q.length) {
    let cur = q.shift();
    for (let i of graph[cur]) {
      if (!bfs_result.includes(i)) {
        q.push(i);
        bfs_result.push(i);
      }
    }
  }
};

dfs(v);
bfs(v);
console.log(...dfs_result);
console.log(...bfs_result);
