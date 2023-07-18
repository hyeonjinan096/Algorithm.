function solution(e) {
    let len = e.length;
    let set = new Set();
    let sum = e.reduce((s,cv)=>s+cv,0)
    set.add(sum);
    e = e.concat(e);
    console.log(e);
    
    for(let i=1;i<=parseInt(len/2);i++){
        for(let j=0;j<len;j++){
            set.add((e.slice(j,j+i)).reduce((sum,cv)=>sum + cv,0));
            set.add(sum - (e.slice(j,j+i)).reduce((sum,cv)=>sum + cv,0));
        }
    }
    return set.size;
}