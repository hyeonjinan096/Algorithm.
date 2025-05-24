from collections import deque
import math

def solution(numbers):

    N = len(numbers)
    visited = [0] *N
#     bfs로는 백트래킹이 어렵나

    def checkPrime(num):
        num = int(''.join(num))
        if num <= 1:
            return False
        if num == 2:
            return True
        for i in range(2,math.ceil(num**(1/2))+1):
            if num % i == 0:
                return False
        return True
    
    answer = set()
    def dfs(num):
        if checkPrime(num):
            answer.add(int(''.join(num)))
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                dfs(num + [numbers[i]])
                visited[i] = 0
                
    for i in range(N):
        visited[i] = 1
        dfs([numbers[i]])
        visited[i] = 0

    return len(answer)