function solution(n, info) {
    var answer = [-1];
    let lion = new Array(info.length).fill(0);
    let max_lion = 0;
    
    function checkScore(lion){
        let lion_score = 0
        let apeach_score = 0
        
        lion.forEach((v, idx)=>{
            if (v === 0 && info[idx] === 0) return
            else if (v > info[idx]) lion_score += (10-idx)
            else apeach_score+= (10-idx)
        })
        
        return lion_score - apeach_score
    }
    
    function updateNewLion(lion){
        for (let i = lion.length-1 ;i>-1;i--){
            if (lion[i] > answer[i]){
                return true
            } else if (lion[i] < answer[i]){
                return false
            }
        }
        return false
    }
    
    function dfs(n,idx){
        if (n == 0 || idx === info.length-1){
            if (n > 0) lion[info.length-1] = n  
            let lion_apeach = checkScore(lion)

            if (lion_apeach > 0){
                if (lion_apeach > max_lion){
                    max_lion = lion_apeach
                    answer = [...lion]
                } else if (lion_apeach === max_lion){
                    //answer과 비교
                    if (updateNewLion(lion)){
                        answer = [...lion]
                    }
                }
            }
            
            lion[info.length-1] = 0
            return
        }
        
        if (n-(info[idx]+1) >= 0){
            lion[idx] = info[idx]+1
            dfs(n-(info[idx]+1),idx+1)
            lion[idx] = 0
        }
        
        dfs(n,idx+1)
    }
    
    dfs(n,0)
    
    
    return answer;
}

//0아니면 어피치보다 더 많이 
//조건 경우 여러개일 떄는 적은 과녁이 많은 수로
