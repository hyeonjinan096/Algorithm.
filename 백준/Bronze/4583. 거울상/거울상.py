
import sys
input = sys.stdin.readline

self_mirror_list = ["i", "o", "v", "w", "x"]

pair_mirror_list = ["b", "d", "b", "p", "q", "p"] 

while True:
    word = input().rstrip()
    if word == "#": break

    mirror_word = []
    for alphabet in word[::-1]:
        if alphabet in self_mirror_list: 
            mirror_word.append(alphabet)
        elif alphabet in pair_mirror_list: 
            mirror_word.append(pair_mirror_list[pair_mirror_list.index(alphabet) + 1])
        else: 
            print("INVALID")
            mirror_word = [] 
            break
    if mirror_word: 
        print(*mirror_word, sep='')