function solution(s) {
    var answer = '';
    let li = s.split("")
    
    li=li.map((a,i)=>{
        if(i==0 || li[i-1]==' '){
            return a.toUpperCase();}
        else{return a.toLowerCase();}
        });
    
    return li.join("");
}