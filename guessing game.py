import random
x = random.randint(1,100)
print('Добро пожаловать в числовую угадайку')
def is_valid(a):
    return a.isdigit() and 1 <= int(a) <= 100

a = input()
count = 1
while x != a:
    check = is_valid(a)
    if check == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
        a = input()
        count += 1
    elif check == True:
        if int(a) > x:
            print('Слишком много, попробуйте еще раз')
            a = input()
            count += 1
        elif int(a) < x:
            print('Слишком мало, попробуйте еще раз')
            a = input()
            count += 1
        elif int(a) == x:
            break
if int(a) == x:
    print('Вы угадали, поздравляем!')
    print('Количество попыток:', count)
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')