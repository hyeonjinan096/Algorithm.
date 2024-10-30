function solution(n, build_frame) {
    const answer = [];
    
    function isOk() {
        for (const [x, y, a] of answer) {
            if (a === 0) { // Column
                if (
                    y !== 0 &&
                    !answer.some(([px, py, pa]) => px === x && py === y - 1 && pa === 0) &&
                    !answer.some(([px, py, pa]) => px === x - 1 && py === y && pa === 1) &&
                    !answer.some(([px, py, pa]) => px === x && py === y && pa === 1)
                ) {
                    return false;
                }
            } else { // Beam
                if (
                    !answer.some(([px, py, pa]) => px === x && py === y - 1 && pa === 0) &&
                    !answer.some(([px, py, pa]) => px === x + 1 && py === y - 1 && pa === 0) &&
                    !(
                        answer.some(([px, py, pa]) => px === x - 1 && py === y && pa === 1) &&
                        answer.some(([px, py, pa]) => px === x + 1 && py === y && pa === 1)
                    )
                ) {
                    return false;
                }
            }
        }
        return true;
    }
    
    for (const [x, y, a, b] of build_frame) {
        if (b === 1) { // Install
            answer.push([x, y, a]);
            if (!isOk()) {
                answer.pop();
            }
        } else { // Delete
            const index = answer.findIndex(([px, py, pa]) => px === x && py === y && pa === a);
            if (index > -1) {
                answer.splice(index, 1);
                if (!isOk()) {
                    answer.push([x, y, a]);
                }
            }
        }
    }
    
    answer.sort((a, b) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2]);
    
    return answer;
    return answer;
}