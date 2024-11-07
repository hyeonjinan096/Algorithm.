# 앞쪽에서 뒤에랑 비교해서 작으면 거기서 변경 
# 뒤쪽에서 앞에랑 비교해서 크면 거기서 변경
# 최저값이랑 최고값을 계산하게 되니 그떄의 차이를 출력

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    values = list(map(int,input().strip().split(' ')))

    for _ in range(N):
        max_idx = values.index(max(values))
        min_idx = values.index(min(values))
        if values[max_idx]-values[min_idx] <=1:
            break
        values[max_idx] -=1
        values[min_idx] +=1

    print(f'#{test_case} {max(values)-min(values)}')

    
        