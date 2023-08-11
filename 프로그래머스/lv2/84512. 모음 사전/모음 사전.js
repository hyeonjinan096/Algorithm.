function solution(word) {
    var answer = 0;
    let count =0;
    let w = ['A','E','I','O','U'];
    function dfs(s){
        count++;
        if(s == word){answer = count; return;}
        if(s.length == 5){return;}
        for(let i of w){
            dfs(s+i);
        }
        
    }
    for(let i of w){
        dfs(i); 
    }
    return answer;
}