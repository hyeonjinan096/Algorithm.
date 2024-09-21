n = int(input())
tip_list = []
total = 0

for _ in range(n):
    tip = int(input())
    tip_list.append(tip)

tip_list.sort(reverse = True)

for i in range(len(tip_list)):
    give_tip = tip_list[i] - i
    if give_tip < 0:
        give_tip = 0
    total += give_tip

print(total)