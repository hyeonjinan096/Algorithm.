from bisect import bisect_left

N = int(input())

lst = map(int,input().split())
tmp_lst = []


for l in lst:
    idx = bisect_left(tmp_lst, l)
    if idx == len(tmp_lst):
        tmp_lst.append(l)
    else:
        tmp_lst[idx] = l

print(len(tmp_lst))