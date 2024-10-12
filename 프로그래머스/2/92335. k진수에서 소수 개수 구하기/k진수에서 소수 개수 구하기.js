function solution(n, k) {
    var answer = 0;
    var str = ''

    while(n>0){
        str = (n%k).toString() + str
        n = Math.floor(n/k)
    }
    
    let values = str.split('0')
    
    function isPrime(num){
        if(num < 2) return false;
        for (let i =2;i<Math.floor(Math.sqrt(num))+1;i++){
            if(num%i === 0){
                return false
            }
        }
        return true
    }
    for(let value of values) {
        if (value === '') continue
        
        value = Number(value)
        if (isPrime(value)) {
            answer += 1
        }
        
    }
    
    return answer;
}