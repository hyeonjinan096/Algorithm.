function solution(n) {
    var answer = 0;
    let list = Array(n+1).fill(0);
    list[1] = 1;
    list[2] = 2;
    for(i=3;i<=n;i++){
        list[i] =(list[i-1] + list[i-2])% 1234567; 
    }
    return list[n] ;
}


//console.log(solution(1999));
