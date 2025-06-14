def z(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n - 1)  # 현재 정사각형의 반
    area = half * half   # 한 사분면의 크기

    if r < half and c < half:
        return 0 * area + z(n - 1, r, c)          # 좌상
    elif r < half and c >= half:
        return 1 * area + z(n - 1, r, c - half)   # 우상
    elif r >= half and c < half:
        return 2 * area + z(n - 1, r - half, c)   # 좌하
    else:
        return 3 * area + z(n - 1, r - half, c - half)  # 우하


N, R, C = map(int, input().split())
print(z(N, R, C))
