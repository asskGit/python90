import random


print('Игра: Угадай Число! ')
print('Компьютер загадал число от 1 до 20')

secret = random.randint(1, 20)

while True:
    guess = int(input('Попробуй угадать число: '))
    if guess == secret:
        print('Молодец ты угадал')
        break
    elif guess > secret:
        print('Слишком большое число. Попробуй меньше')
    else:
        print('Слишком маленькое число. Попробуй больше')
