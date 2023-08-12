function solution(x, y, n) {
    var answer = 0;
    let li = new Array(y+1).fill(Infinity);
    li[x] = 0;
    for(let i = x;i<=y;i++ ){
        li[i+n] = li[i+n]>li[i]+1 ? li[i]+1:li[i+n];
        li[i*2] = li[i*2]>li[i]*2 ? li[i]+1:li[i*2];
        li[i*3] = li[i*3]>li[i]*3 ? li[i]+1:li[i*3];
    }
    
    return li[y]!=Infinity?li[y]:-1;
}