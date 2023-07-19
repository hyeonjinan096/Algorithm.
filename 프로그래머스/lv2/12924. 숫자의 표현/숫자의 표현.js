function solution(n) {
    // 1개로 자신을 표현하는 수는 미리 추가 
    let answer = 1
    for(let i=1;i<n/2;i++){
        let sum = i
        for(let j=i+1;j<n;j++){
            sum += j
            if(sum === n){
                answer++
                break;
            }
            else if(sum  > n){
                break;
            }
        }
    }

    return answer
}