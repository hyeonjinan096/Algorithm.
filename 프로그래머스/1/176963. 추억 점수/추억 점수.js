function solution(name, yearning, photo) {
    var answer = [];
    const data = {}
    for(let i in name) {
        data[name[i]] = yearning[i]
    }
     
    return photo.map(
        (arr)=> arr.reduce((acc, cur)=> acc + (data[cur] ||0), 0)
    )
    
    return answer;
}