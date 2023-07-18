function solution(A,B){
    var answer = 0;
    A = A.sort((a,b)=>a-b);
    B = B.sort((a,b)=>b-a);
    
    
    return A.map((a,i)=> a*B[i]).reduce((s,cv)=>s+cv,0);
}