function solution(elements) {
    var answer = 0;
    let set = new Set();
    let E = elements+"," + elements;
    let k;
    E = E.split(",");
    E = E.map((e)=>parseInt(e));
    let sum;
    
    for(let i in elements){
        for(let j in elements){
            k = E.slice(j,parseInt(i)+parseInt(j)+1)
            sum = (k.reduce((s,c)=>s+c,0));
            set.add(sum);
        }
    }
    
    return set.size;
}