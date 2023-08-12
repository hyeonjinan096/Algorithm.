function solution(elements) {
    var answer = 0;
    let e = elements.concat(elements);
    let arr;
    let set = new Set();
    
    for(let i =0;i<elements.length ;i++){
        for(let j=0;j<elements.length;j++){
            arr = e.slice(j,j+i+1);
            set.add(arr.reduce((s,c)=>s+c,0));
        }
    }
    
    return set.size;
}