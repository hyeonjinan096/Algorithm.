const fs = require("fs");
const input = fs.readFileSync('/dev/stdin', "utf8").trim().split("\n");

const [N, Q] = input.shift().split(" ").map(Number);
let graph = [...Array(N)].map(() => Array());

for (let i = 0; i < N - 1; i++) {
  const [a, b, r] = input.shift().split(" ").map(Number);
  graph[a - 1].push([b - 1, r]);
  graph[b - 1].push([a - 1, r]);
}

const bfs = (v, k) => {
  let q = [v];
  let visited = Array(N).fill(0);
  visited[v] = 1;
  let cnt = 0;

  while (q.length) {
    const cur_v = q.shift();
    for (let [next_v, r] of graph[cur_v]) {
      if (!visited[next_v]) {
        if (r >= k) {
          q.push(next_v);
          cnt += 1;
          visited[next_v] = 1;
        }
      }
    }
  }

  return cnt;
};

for (let i = 0; i < Q; i++) {
  const [k, v] = input.shift().split(" ").map(Number);

  console.log(bfs(v - 1, k));
}
