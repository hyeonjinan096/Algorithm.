function solution(n) {
    var answer = 0;
    let li = new Array(n+1).fill(0);
    li[1] = 1;
    li[2] = 2;
    for(let i =3;i<=n;i++){
        li[i] = (li[i-1]+li[i-2])% 1234567;
    }

    return li[n] % 1234567;
}