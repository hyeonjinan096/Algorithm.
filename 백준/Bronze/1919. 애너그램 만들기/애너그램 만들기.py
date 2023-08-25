
alphabet = 'abcdefghijklmnopqrstuvwxyz'
map = {}
for abc in alphabet:
    map[abc] = 0

word1 = input()
for i in word1:
    map[i] += 1

word2 = input()
for i in word2:
    map[i] -= 1

ans = 0
for i in map:
    ans += abs(map[i])

print(ans)