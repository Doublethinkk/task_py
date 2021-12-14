import random
x = random.randrange(0, 101)
b = (input("введите число :  "))
cnt = 0
while x != b:
    if b.isdigit():
        cnt += 1
        if x > int(b):
            print("ошибка.заданное число больше")
        elif x < int(b):
            print("ошибка.заданное число меньше")

        if x == int(b):
            print("победа")
            print("зааданное число : ", x)
            cnt += 1
            print("число попыток : ", cnt)
            break
        b = (input("enter "))

    else:
        print("ошибка. вы ввели не число")
        b = (input("enter "))
