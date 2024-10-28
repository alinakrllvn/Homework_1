# Your code here (˶ˆᗜˆ˵)

n = int(input())
x, y = 0, 0
for _ in range(n):
    inp = input()
    if inp == "Вверх":
        y += 1
    elif inp == "Вниз":
        y -= 1
    elif inp == "Вправо":
        x += 1
    elif inp == "Влево":
        x -= 1
    else:
        print('Не тупи, пожалуйста')
print(abs(x) + abs(y))