function solution(n) {
    var answer = 1;
    let sum=0;
    for(let i =1;i<n/2;i++){
        sum +=i;
        for(let j =i+1;j<n;j++){
            sum +=j;
            if(sum ==n){ answer++;}
            else if(sum>n){break;}
        }
        sum =0;
    }
    return answer;
}