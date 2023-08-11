function solution(n) {
    var answer = 0;
    let li=new Array(n+1).fill(0);
    li[0] = 0;
    li[1] = 1;
    for(let i=2;i<=n;i++){
        li[i] = li[i-1]%1234567+li[i-2]%1234567;
    }
    return li[n] %1234567;
}