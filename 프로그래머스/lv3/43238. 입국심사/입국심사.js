function solution(n, times) {
    var answer = 0;
    return function solution(n, times) {
    let left = 1;
    let right = Math.max(...times) * n; // 이진 탐색의 시작과 끝 범위 설정

    let answer = 0;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2); // 중간값을 구함
        let count = 0;

        // 중간값(mid) 시간 동안 각 심사관이 몇 명을 처리할 수 있는지 계산
        for (const time of times) {
            count += Math.floor(mid / time);
        }

        // 처리한 사람 수(count)가 대기하는 사람 수(n)보다 작으면
        // 시간을 늘려서 처리할 수 있는지 확인
        if (count < n) {
            left = mid + 1;
        } else {
            answer = mid;
            right = mid - 1;
        }
    }

    return answer;
}answer;
}