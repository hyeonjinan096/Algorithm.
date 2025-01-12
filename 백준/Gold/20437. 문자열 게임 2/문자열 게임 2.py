from collections import deque

# 테스트 케이스 개수 입력
T = int(input())
for _ in range(T):
    W = input()  # 문자열 입력
    K = int(input())  # 찾고자 하는 문자열의 길이
    char_indices = {}  # 각 문자의 인덱스를 저장하는 딕셔너리
    min_length = float("inf")
    max_length = 0

    for idx, char in enumerate(W):
        if char not in char_indices:
            char_indices[char] = deque()
        char_indices[char].append(idx)

        # deque의 크기가 K보다 커지면 앞에서 제거
        if len(char_indices[char]) > K:
            char_indices[char].popleft()

        # deque의 크기가 K일 때, 최소 및 최대 길이 계산
        if len(char_indices[char]) == K:
            length = char_indices[char][-1] - char_indices[char][0] + 1
            min_length = min(min_length, length)
            max_length = max(max_length, length)

    # 결과 출력
    if min_length == float("inf") and max_length == 0:
        print(-1)
    else:
        print(min_length, max_length)