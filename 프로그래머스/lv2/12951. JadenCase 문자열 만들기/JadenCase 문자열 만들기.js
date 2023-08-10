function solution(s) {
    var answer = '';
    let k =0;
    S= s.split('');
    answer=S.map((e)=>{
        if(k==0 && e.toLowerCase() == e){e=e.toUpperCase();}
        else if(k==1 && e.toUpperCase()==e){e=e.toLowerCase();}
        k=1;
        if(e==' '){k=0;}
        return e;
    })
    return answer.join("");
}