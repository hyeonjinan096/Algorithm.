function solution(numbers) {
    var answer = 0;
    
    let Num = Array.from(numbers);
    Num =Num.map((e)=>parseInt(e))
    
    function check(n){
        let k = n>4 ? n/2 : n;
        for(let i =2 ;i<k ;i++){
            if(n%i ==0){return 0;}
        }
        if(n ==1 ||n==0){return 0;}
        return 1;
    }
    
    let set = new Set();
    let visited = Array(numbers.length).fill(0);
    
    
    function dfs(num,y){
        //console.log(num);
        if(!set.has(num)){
            if(check(num)){
                //console.log(num+"소수");
                answer++;}
            set.add(num);}
        for(let i in Num){
            if(visited[i]==0){
                //console.log(Num[i]+'방문 안함')
                visited[i] =1;
                dfs(num+(y*10)*Num[i],y*10);
                visited[i] =0;
            }
        }
        return;
    }
    
    for(let i in Num){
        visited[i] = 1;
        dfs(Num[i],1);
        visited[i] = 0;
    }
    
    console.log(set);
    return answer;
}
console.log(solution("1234"));