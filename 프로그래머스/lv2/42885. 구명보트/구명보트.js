function solution(people, limit) {
    var answer = 0;
    p=people.sort((a,b)=>a-b);
    
    for(let i=0;i<p.length;i++){
        for(let j=p.length-1;j>=i;j--){
            if(i==j){
                answer++;
            }
            else if(p[i] +p[j] > limit){
                answer++;
                p.pop();
            }
            else{
                answer++;
                p.pop();
                break;
            }
            
        }
    }
    
    return answer;
}