message = input()
happy = sad = 0
for i in range(0, len(message) - 2):
    if message[i] == ':' and message[i + 1] == '-':
        if message[i + 2] == ')':
            happy += 1
        elif message[i + 2] == '(':
            sad += 1

if happy == 0 and sad == 0:
    print('none')
else:
    if happy > sad:
        print('happy')
    elif happy < sad:
        print('sad')
    else:
        print('unsure')