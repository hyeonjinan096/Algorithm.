function solution(s) {
    let a = s.split("");
    let k = 0;
    
    for(let i = 0; i< a.length; i++){
        
        if(k == 0 || a[i-1]==' '){
            a[i] = a[i].toUpperCase();
            k=1;
        }
        else if(k!=0){
            a[i] = a[i].toLowerCase();
        }
        else if(a[i] === " "){
            k =0;
        }
    }
    
    return a.join("");
}