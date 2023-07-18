function solution(A,B){
    var answer = [];
    A = A.sort((a,b)=>a-b);  //배열 오름차순 정렬
    B = B.sort((a,b)=>b-a);  //배열 내림차순 정렬
    for(let i = 0;i<A.length;i++){
       answer.push(A[i]*B[i]);  //배열에 추가 하기 push
    }
    result = answer.reduce((sum,cv) =>sum+cv,0);  //reduce ->sum . avg 가능 
    
    return result;
}