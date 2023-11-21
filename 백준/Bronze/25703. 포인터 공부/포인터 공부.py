def fun(n):
    print('int a;')
    print('int *ptr = &a;')
    if n == 2 or n >= 3:
        print('int **ptr2 = &ptr;')
        for i in range(3, n + 1):
            star = '*' * i
            print('int %sptr%d = &ptr%d;' % (star, i, i - 1))

n = int(input())
fun(n)
