function solution(users, emoticons) {
    var answer = [0,0];
    
    function permutation(arr, repeat) {
        const result = [];
        if (repeat === 1) return arr.map(v => [v]);
        arr.forEach((v) => {
            const fixed = v;
            const permuArr = permutation(arr, repeat - 1); // 재귀 호출
            const comArr = permuArr.map((p) => [fixed, ...p]); // fixed를 조합에 추가
            result.push(...comArr); // 전체 결과에 추가
        });
        return result;
    }
    
    let sale_datas = permutation([10,20,30,40],emoticons.length)
    
    for (let sale_data of sale_datas){
        let result = [0,0]
        
        users.forEach(([user_sale,user_cost])=>{
            let [join, cost] = [0,0]
            
            for (let i in emoticons){
                let price = emoticons[i]
                if (user_sale <= sale_data[i]){
                    cost += price * ((100-sale_data[i])/100)
                }
                if (user_cost <= cost){
                    cost = 0
                    join = 1
                    break
                }
            }
            
            result[0]+=join
            result[1]+=cost
        })
        
        if (result[0] > answer[0]){
            answer = [...result]
        } else if (result[0] === answer[0] && result[1]>answer[1]){
            answer = [...result]
        }
        
    }
    
    return answer;
}