function solution(friends, gifts) {
    let N = friends.length
    var answer = new Array(N).fill(0);
    let gifts_log = [...Array(N)].map(()=> Array(N).fill(0))
    let gifts_num = new Array(N).fill(0)
    //gifts를 이중 배열로 정리
    //gifts 비교해서 선물 지수 배열로 정리 
    
    
    gifts.forEach((v)=> {
        let [from, to] = v.split(" ").map((v)=> friends.indexOf(v))
        gifts_log[from][to] += 1
        gifts_num[from] +=1
        gifts_num[to] -=1
    })
    //이중 탐색으로 서로 비교해서 받는 선물 정리 
    //배열 먼저 탐색 , 선물 지수 탐색 
    
    for (let i =0;i<N;i++){
        for (let j = i+1;j<N;j++){
            if (gifts_log[i][j] > gifts_log[j][i]){
                answer[i] +=1
            } else if(gifts_log[i][j] < gifts_log[j][i]){
                answer[j] +=1
            } else if (gifts_num[i] > gifts_num[j]){
                answer[i] +=1
            } else if (gifts_num[i] < gifts_num[j]){
                answer[j] +=1
            }
        }
    }
    
    //결과에서 max값 출력
    return Math.max(...answer);
}



//두 사람 선물 주고 받은 기록 -> 많은 사람이 받는 거 
//기록 없거나 같으면 -> 선물 지수 큰 사라미 받는 거 
//섬눌 지수 이번달까지 준 거 - 받은 선물 (손해 받은 값)
//선물 지수도 같으면 걍 주고 받기 마삼

//섬루 가장 많이 받을 친구 선물 수 
//from to