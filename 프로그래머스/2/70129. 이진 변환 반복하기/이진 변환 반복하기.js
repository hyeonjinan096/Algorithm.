//10.07
function solution(s) {
    var answer = [0,0];
    
    while(1){
        answer[0]++
        answer[1] += (s.match(/0/g)||[]).length;
        s = s.split('0').join('').length.toString(2)
        // s = s.replace(/0/g,'').length.toString(2)

        if(s === '1'){
            return answer
            break
        }
    }
}