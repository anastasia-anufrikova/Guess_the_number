import random

x = random.randint(1, 100)
print('Введите число')
a = int(input())
while a != x:
    if a > x:
        print('Слишком много, попробуйте еще раз')
        a = int(input())
    elif a < x:
        print('Слишком мало, попробуйте еще раз')
        a = int(input())
if a == x:
    print('Вы угадали, поздравляем!')