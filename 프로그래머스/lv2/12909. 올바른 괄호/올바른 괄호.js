function solution(s){
    
    let stackCount =0;
    for (let i of s){
        if(i == "("){stackCount+=1;}
        else{stackCount-=1;}
        if(stackCount < 0){return false;}
    }
    if(stackCount!=0){return false;}
    else {return true;}
    //console.log(typeof(answer)); ->boolean
}