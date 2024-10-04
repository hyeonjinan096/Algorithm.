def solution(n, info):
    answer = [-1]
    #화살이 없거나 과녁 다 맞추면 점수 계산 
    #점수 비교 후 라이언이 이겼고 그 점수 차가 Max보다 크다면 answer에 라이언 값 갱신
    #점수 차가 같다면 answer과 라이언 값을 비교 뒤에서 부터 비교 (뒤쪽부터 비교해서 하나라도 차이나면 결과 반환 후 break)
    # answer 출력 
    #끝까지 점수를 내야하기 떄문에 dfs(cnt,lion)
    lion = [0]*11
    Max = 0
    
    def check():
        L = 0
        A = 0
        for i in range(11):
            if lion[i]>info[i]:
                L+=(10-i)
            elif info[i]!=0 and lion[i]<=info[i]:
                A+=(10-i)
        return L>A, abs(L-A)
    
    def dfs(cnt, idx):
        nonlocal Max, answer
        if cnt == 0 or idx == 10:
            lionWin, gap = check()
            if lionWin:
                lion[10] = cnt
                if Max < gap:
                    Max = gap
                    answer = lion[:]
                elif Max == gap:
                    for i in range(10,-1,-1):
                        if lion[i]>answer[i]:
                            print(lion)
                            answer = lion[:]
                            break
                        elif answer[i]>lion[i]:
                            break
                lion[10] = 0
            return
        if cnt-(info[idx]+1)>=0:
            lion[idx] = info[idx]+1
            dfs(cnt-(info[idx]+1), idx+1)
            lion[idx] = 0
        dfs(cnt,idx+1)
                        
            #비교
            #cnt남은 거 처리 
    dfs(n,0)
    return answer