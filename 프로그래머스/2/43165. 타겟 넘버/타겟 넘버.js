function solution(numbers, target) {
    var answer = 0;
    dfs = (a,l) =>{
        if(l == numbers.length){
            if(a == target){ answer+=1}
            return
        }
        dfs(a + numbers[l],l+1)
        dfs(a - numbers[l],l+1)
    }
    dfs(numbers[0],1)
    dfs(-numbers[0],1)
    return answer;
}