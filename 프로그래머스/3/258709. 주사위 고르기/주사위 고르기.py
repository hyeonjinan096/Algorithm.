from itertools import combinations, product
from bisect import bisect_left
def solution(dice):
    answer = []
    #n개의 주사위 
    n = len(dice)
    Max = 0
    
    
    for a_com in combinations(range(n),n//2):
        b_com = [j for j in range(n) if j not in a_com]
        A, B = [],[]
        
        for dice_com in product(range(6),repeat=n//2):
            A.append(sum(dice[i][j] for i,j in zip(a_com, dice_com)))
            B.append(sum(dice[i][j] for i,j in zip(b_com, dice_com)))
        B.sort()
        wins = 0
        for a in A:
            wins+=bisect_left(B,a)
        if Max < wins:
            answer = a_com
            Max = wins

    return [i+1 for i in answer]

    #n개의 주사위를 2분류로 나눠야함 
    #나눈 경우에 나올 수 있는 모든 합을 구해야함 
    #각각 나온 모든 합을 이용해서 승패를 계산 해야함 (이분탐색)
    #승이 높은 경우의 조합으로 출력해야함 