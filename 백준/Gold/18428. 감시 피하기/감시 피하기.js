const fs = require("fs");
const input = fs.readFileSync('/dev/stdin', "utf8").trim().split("\n");
const n = input.shift();
const graph = [];

for (let i = 0; i < n; i++) {
  graph.push(input.shift().trim().split(" "));
  for (let j = 0; j < n; j++) {
    if (graph[i][j] === "X") {
      graph[i][j] = 0;
    }
  }
}

const check = () => {
  let dir = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (graph[i][j] === "T") {
        let flag = 0;
        for (let [dx, dy] of dir) {
          let nx = i + dx;
          let ny = j + dy;

          if (0 <= nx && nx < n && 0 <= ny && ny < n) {
            if (graph[nx][ny] === "S") {
              return "NO";
            }
          }
          while (0 <= nx && nx < n && 0 <= ny && ny < n) {
            if (graph[nx][ny] === "S") {
              flag = 1;
              break;
            }
            nx += dx;
            ny += dy;
          }
          nx = i + dx;
          ny = j + dy;
          if (flag) {
            while (0 <= nx && nx < n && 0 <= ny && ny < n) {
              if (graph[nx][ny] === "S") {
                break;
              }
              graph[nx][ny] += 1;
              nx += dx;
              ny += dy;
            }
            flag = 0;
          }
        }
      }
    }
  }

  for (let i = 0; i < 3; i++) {
    const max = [0, 0, 0];
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (typeof graph[i][j] === "number" && graph[i][j] > max[0]) {
          max[0] = graph[i][j];
          max[1] = i;
          max[2] = j;
        }
      }
    }

    let flag = 0;
    for (let [dx, dy] of dir) {
      let nx = max[1];
      let ny = max[2];
      while (0 <= nx && nx < n && 0 <= ny && ny < n) {
        if (graph[nx][ny] === "S" || graph[nx][ny] === "T") {
          flag = 1;
          break;
        }
        nx += dx;
        ny += dy;
      }
      nx = max[1];
      ny = max[2];
      if (flag) {
        while (0 <= nx && nx < n && 0 <= ny && ny < n) {
          if (graph[nx][ny] === "S" || graph[nx][ny] === "T") {
            break;
          }
          graph[nx][ny] = 0;
          nx += dx;
          ny += dy;
        }
        flag = 0;
      }
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (typeof graph[i][j] === "number" && graph[i][j] !== 0) {
        return "NO";
      }
    }
  }
  return "YES";
};

console.log(check());
