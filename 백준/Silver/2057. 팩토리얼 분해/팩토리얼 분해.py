n = int(input())
if n == 0:
    print("NO")
    exit()

def dfs(current_sum, index):
    if current_sum == n:
        return True
    if current_sum > n or index > 20:
        return False
    if dfs(current_sum + fac[index], index + 1):
        return True
    if dfs(current_sum, index + 1):
        return True
    return False

fac = [1]
for i in range(1, 21):
    fac.append(fac[-1] * i)

if dfs(0, 0):
    print("YES")
else:
    print("NO")


