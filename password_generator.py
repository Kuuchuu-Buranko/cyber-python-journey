import random

length = int(input("Длина пароля: "))
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password = ""
for _ in range(length):
    password += random.choice(chars)

print(f"Ваш пароль: {password}")