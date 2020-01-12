def number():
    num = int(input('Введите число: '))
    if 10 % num != 0:
        print(10 % num)
    else:
        print(num)
number()