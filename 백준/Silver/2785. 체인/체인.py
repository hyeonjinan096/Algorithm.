
def check(chains):
    if len(chains) == 2:
        return 1

    n = len(chains)
    answer= 0
    for chain in chains:
        n-=1
        key = chain
        if n <= key:
            return answer + n
        elif n > key:
            n -= key
            answer += key
        if n == 1:
            return answer



N = int(input())
chains = list(map(int,input().split()))
chains.sort()


print(check(chains))