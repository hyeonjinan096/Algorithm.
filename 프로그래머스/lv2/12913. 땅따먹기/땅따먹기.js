//dp
function solution(land) {
    var answer = 0;
    let k ;
    let max;
    
    for(let i in land){
        //console.log("c"+i);
        if(i == 0){continue;}
        for(let j in land[i]){
            //console.log("z"+j);
            k =[]
            k=k.concat(land[i-1]);
            k[j] = -1;
            //console.log(k);
            land[i][j] += Math.max(...k);
        }
        max =Math.max(...land[i]);
    }
    
    return max;
    
}
//let j = [1,2,2];
//console.log(j.lastIndexOf(2));
//console.log(solution([[1,1,2,2],[1,2,4,0]]))