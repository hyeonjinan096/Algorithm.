from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    answer = []
    n = len(dice)
    Max = 0
    
    for a_com in combinations(range(n),n//2):
        b_com = [a for a in range(n) if a not in a_com]
        
        a_sum, b_sum = [],[]
        for j in product(range(6),repeat = n//2):
            a_sum.append(sum(dice[x][y] for x,y in zip(a_com, j)))
            b_sum.append(sum(dice[x][y] for x,y in zip(b_com, j)))
        b_sum.sort()
        wins = 0
        for a in a_sum:
            wins += bisect_left(b_sum, a)
        if wins > Max:
            Max = wins
            answer = a_com
            
            
        
    
    
    return [x+1 for x in answer]


#주사위 종류 2개 조합 cobinations
#주사위 2개에서 만들 수 있는 합  몇번째가 나오는 지 조합  permutations 
# 두 주사위 합 모두 비교 -> 경우의 수 쌓임 가장 높은 경우 저장 