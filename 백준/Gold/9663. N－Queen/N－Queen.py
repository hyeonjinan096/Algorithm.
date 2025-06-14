N = int(input())
count = 0

col_used = [False] * N
diag1 = [False] * (2*N)
diag2 = [False] * (2*N)

def solve(row):
    global count

    if row == N:
        count += 1
        return 
    
    for col in range(N):
        if col_used[col] or diag1[row + col] or diag2[row - col + N -1]:
            continue
        col_used[col] = diag1[row + col] = diag2[row - col + N -1] = True
        solve(row + 1)
        col_used[col] = diag1[row + col] = diag2[row - col + N - 1] = False

solve(0)
print(count)