#0이 생기면 0으로 저장하고 그게 암호 됨요

# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test = int(input())
    values = list(map(int,input().strip().split(' ')))
    n = len(values)

    stop_flag = 0
    while(1):
      for i in range(1,6):
        tmp = values.pop(0) - i
        if tmp <= 0:
          tmp = 0
        values.append(tmp)
        if tmp == 0:
          stop_flag = 1
          break
      if stop_flag:
        break
    
    print(f'#{test_case} ',end='')
    print(*values)
    