color1 = input()
color2 = input()
color3 = input()
color_value = {'black' : 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
               'green': 5, 'blue': 6, 'violet' : 7, 'grey': 8, 'white': 9}

print((color_value[color1]*10 + color_value[color2]) * (10 ** color_value[color3]))