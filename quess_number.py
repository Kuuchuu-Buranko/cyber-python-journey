import random
secret = random.randint(1,100)
attempts = 0

print("Я загадал число от 1 до 100. Попробуй угадать!: ")

while True:
    quess = int(input("Твое число: "))
    attempts += 1

    if quess < secret:
        print("Больше!")
    elif quess > secret:
        print("Меньше!")
    else:
        print(f"Ты угадал! Это {secret}. Попыток: {attempts}")
        break