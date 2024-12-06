function solution(n) {
    var answer = 0;
    let N = n.toString(2)
    let idx = N.lastIndexOf('01')
    N = N.split('')
    
    if (idx === -1){
        answer = ['1','0', ...N.slice(1).sort()].join('')
    } else {
        N[idx] = '1'
        N[idx+1] = '0'
        answer = [...N.slice(0,idx+2), ...N.slice(idx+2).sort()].join('')
        
    }
    return parseInt(answer,2);
}
