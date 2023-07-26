function solution(s) {
    var answer = '';
    li = s.split(" ");
    answer = Math.min(...li)+ " " +Math.max(...li);
    return answer;
}