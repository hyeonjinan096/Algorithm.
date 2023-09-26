function solution(n, edges) {
    const graph = {}; // 그래프의 인접 리스트
    const visited = Array(n + 1).fill(false); // 방문 여부를 나타내는 배열
    const distances = Array(n + 1).fill(0); // 1번 노드로부터의 거리 배열

    // 그래프 생성
    for (const [from, to] of edges) {
        if (!graph[from]) {
            graph[from] = [];
        }
        if (!graph[to]) {
            graph[to] = [];
        }
        graph[from].push(to);
        graph[to].push(from);
    }

    // BFS 수행
    const queue = [1]; // 시작 노드인 1번 노드를 큐에 추가
    visited[1] = true;

    while (queue.length > 0) {
        const node = queue.shift();

        for (const neighbor of graph[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                distances[neighbor] = distances[node] + 1;
                queue.push(neighbor);
            }
        }
    }

    // 최대 거리 구하기
    const maxDistance = Math.max(...distances.slice(1));

    // 최대 거리에 해당하는 노드 개수 세기
    return distances.filter(distance => distance === maxDistance).length;
}
