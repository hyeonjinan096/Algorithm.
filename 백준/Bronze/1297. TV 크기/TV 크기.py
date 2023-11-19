d, h, w = map(int, input().split())
H =  int((h*d) / (((h**2) + (w**2)) **(1/2)))
W =  int((w*d) / (((h**2) + (w**2)) **(1/2)))
print(H, W)