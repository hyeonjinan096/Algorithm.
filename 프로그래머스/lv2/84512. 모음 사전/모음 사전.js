function solution(word) {
    var answer = 0;
    let arr=[];
    let li = ['A','E','I','O','U'];
    let result;
    function dfs(i,n,arr){
        answer++;
        if(arr == word){
            result=answer;
            //console.log(answer);
        }
        if(n>4){return;}
        for(let j of li){
            dfs(j,n+1,arr+j);
            i++;
        }
    }
    
    for(let i of li){
        dfs(i,1,i);
    }
    return result;
}