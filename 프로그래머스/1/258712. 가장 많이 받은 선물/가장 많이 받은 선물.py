def solution(friends, gifts):
    answer = 0
    N = len(friends)
    table = [[0]*N for _ in range(N)]
    values = [0]*N
    result = [0]*N
    for gift in gifts:
        f,t = gift.split()
        F,T = friends.index(f), friends.index(t)
        table[F][T] += 1
        values[F]+=1
        values[T]-=1
        
    for i in range(N):
        for j in range(i+1, N):
            if table[i][j] > table[j][i]:
                result[i]+=1
            elif table[i][j] < table[j][i]:
                result[j]+=1
            elif values[i] > values[j]:
                result[i]+=1
            elif values[i] < values[j]:
                result[j]+=1
            
    return max(result)