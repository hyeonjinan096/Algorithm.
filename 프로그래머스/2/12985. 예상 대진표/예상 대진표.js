//11:39
function solution(n,a,b)
{
    var answer = 0;
    while(1){
        answer++
        a = Math.max(Math.ceil(a/2),1)
        b = Math.max(Math.ceil(b/2),1)
        if(a === b){break}
    }
    
    return answer;
}

solution(10,1,7)


