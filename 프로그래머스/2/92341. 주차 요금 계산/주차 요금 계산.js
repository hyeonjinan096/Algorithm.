function solution(fees, records) {
    var answer = [];
    let parking = new Map();
    let data = {};
    const [b_t, b_f, p_t, p_f] = fees
    for(let record of records){
        const [time, car, io] = record.split(' ')
        const [h,m] = time.split(':').map(e=> Number(e))
        t = h*60 + m
        
        if(io === 'IN'){
            parking.set(car,t)
        }
        else{
            if(data[car]){
                data[car]+=t - parking.get(car)
            }else{
                data[car] = t - parking.get(car)
            }
            parking.delete(car);
        }
    }
    
    for(let [car,time] of parking){
        if(data[car]){
            data[car]+=(23*60 + 59) - time
        }else{
            data[car]=(23*60 + 59) - time
        }
    }
    const sortedResult = Object.entries(data).sort((a, b) => a[0].localeCompare(b[0]));


    // 요금 계산
    for (const [car, time] of sortedResult) {
        const totalFee = b_f + Math.ceil(Math.max(0, time - b_t) / p_t) * p_f;
        answer.push(totalFee);
    }

    return answer;
}