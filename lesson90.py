import random
import time
import pyfiglet

title = pyfiglet.figlet_format('Ugaday Chislo!')
print(title)

print("Компьютер загадал число от 1 до 20...")
time.sleep(1.5)
print("У тебя есть 5 попыток, чтобы угадать \n")
time.sleep(1)

secret = random.randint(1,20)

attempts = 0
max_attempts = 5

while True:
    guess = int(input("Введите число: "))
    attempts += 1
    left = max_attempts - attempts

    time.sleep(0.5)

    if guess == secret:
        print(f"\n Молодец ты угадал число {secret} за {attempts} попыток")
        break
    elif guess > secret:
        print(f"Слишком большое, попробуй меньше, Осталось {left} попыток \n " )
    else:
        print(f"Слишком маленькое, попробуй больше, Осталось {left} попыток \n " )

    time.sleep(1)

    if attempts == max_attempts:
        print(f"у тебя закончились попытки, Загаданное число было {secret}")
        break

time.sleep(1)
print('Спасибо за игру')


