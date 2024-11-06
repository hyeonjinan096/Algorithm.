T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    values = list(map(int,input().split(' ')))

    answer = 0
    for i in range(2,len(values)-2): 
        result = float('inf')
        for j in [i-2,i-1,i+1,i+2]:
            result = min(result,values[i]-values[j])
        if result > 0:
            answer+=result
    print(f'#{test_case} {answer}')

