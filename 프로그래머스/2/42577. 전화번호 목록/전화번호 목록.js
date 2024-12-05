// 1,000,000 -> O(n)
function solution(phone_book) {
    phone_book.sort()
    for (let i=0;i<phone_book.length-1;i++){
        let reg = RegExp('^'+phone_book[i])
        if (reg.test(phone_book[i+1])){
           return false
       }  
    }
    return true;
}