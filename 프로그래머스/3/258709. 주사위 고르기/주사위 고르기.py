from itertools import combinations, product
from bisect import bisect_left

def solution(dices):
    dic = {}
    L = len(dices)
    for A_index_combi in combinations(range(L), L//2):
        B_index_combi = [i for i in range(L) if i not in A_index_combi]
        print(A_index_combi)
        A, B = [], []
        for order_product in product(range(6), repeat=L//2):
            # A_index_combi : 주사위 번호
            # order_product: 주사위 면 번호
            # zip(A_index_combi, order_product) : 주사위 마다 면 번호 i,j -> 주사위마다 면번호의 값을 sum으로 더함
            A.append(sum(dices[i][j] for i, j in zip(A_index_combi, order_product)))
            B.append(sum(dices[i][j] for i, j in zip(B_index_combi, order_product)))
        B.sort()
        
        wins = 0
        for i in A:
            l, r = 0,len(B)-1
            while(l<=r):
                mid = (l+r)//2
                if B[mid] >= i:
                    result = mid
                    r = mid-1
                else:
                    l = mid+1
            wins+=l
        
        
            

        # wins = sum(bisect_left(B, num) for num in A)
        dic[wins] = list(A_index_combi)

    max_key = max(dic.keys())

    return [x+1 for x in dic[max_key]]