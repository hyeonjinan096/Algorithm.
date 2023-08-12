function solution(want, number, discount) {
    var answer = 0;
    let arr =[];
    let N ;
    for(let i=0;i<discount.length;i++){
        arr = discount.slice(i,i+10);
        N = [...number]
        for(let j in want){
            while(arr.includes(want[j])){
                N[j]--;
                arr[arr.indexOf(want[j])] = 0;
            }
        }
        if(Math.max(...N)<=0){answer++;}
    }
    return answer;
}