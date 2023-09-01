name = input()
N = int(input())
list = []
A = []

for i in range(N):
    list.append(input())
    L = name.count("L") + str(list[i]).count("L")
    O = name.count("O") + str(list[i]).count("O")
    V = name.count("V") + str(list[i]).count("V")
    E = name.count("E") + str(list[i]).count("E")
    num = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    A.append((num, list[i]))
    
A.sort(key=lambda q : (-q[0], q[1]))

print(A[0][1])