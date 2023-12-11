function solution(players, callings) {
    var answer = [];
    let dic = {};
    for (let i in players) {
        dic[players[i]] = i;
    }
        
    
    for (let player of callings){
        n = dic[player]
        dic[player] = n-1
        dic[players[n-1]] = n
        c = players[n]
        players[n] = players[n-1]
        players[n-1] = c
    }
        
    
    return players;
}