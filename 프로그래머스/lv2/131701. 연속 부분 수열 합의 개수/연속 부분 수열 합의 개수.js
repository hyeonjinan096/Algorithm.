function solution(e) {
    let s = [];
    let set = new Set();
    let k;
    let sum =e.reduce((sum,cv)=>sum+cv,0);
    set.add(sum);
    let len = e.length
    
    for(let i = 1 ; i <= parseInt(len/2);i++){
        for(let j=0; j<len;j++){
            if(i+j <len){ k = (e.slice(j,(j+i)).reduce((sum,cv)=>sum+cv,0));}
            else{
                 k = (e.slice(j).concat(e.slice(0, j+i-len)).reduce((sum,cv)=>sum+cv,0));
                
            }
            set.add(k);
            set.add(sum-k);
            
            //if(s.findIndex((a)=>a==k)==-1){s.push(k);}
            //if(s.findIndex((a)=>a==(sum-k))==-1){s.push(sum-k);}
            
        }
    }
    
    
    return set.size;
}
