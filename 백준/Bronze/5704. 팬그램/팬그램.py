import sys

while True:
    s = sys.stdin.readline().strip()
    if s == "*":
        break
    else:
        list = set(s.replace(" ", "").lower())
        if len(list) == 26:
            print("Y")
        else:
            print("N")
