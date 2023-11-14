import random

#1

a = 5
b = 4
for i in range(b):
    a += 1
print(a)    

#2

a = 3
b = 5
for i in range(b):
    a *= 2
print(a) 

#3

a = 24
while a % 2 == 0:
     a /= 2
     print(a)
print("Число не є парним")   

#4

a = int(input("Введіть ціле число: "))
while a < 100:
     a += 5
     print(a)

#5

a = random.randint(0, 10)
while True:  
    b = int(input("Вгадайте ціле число: "))
    if b == a:
        print("Вітаємо!")
        break
    else:
        print("Спробуйте ще раз")

#6

a = int(input("Загадайте ціле число: "))
print("\n" * 100)
while True:  
    b = int(input("Вгадайте ціле число: "))
    if b == a:
        print("Вітаємо!")
        break
    else:
        print("Спробуйте ще раз") 

#7

a = 5
b = 0
for i in range(5):
    b += a
    a += 2
print(b)

#8

a = int(input("Введіть ваше число: "))
n = int(input("Скільки чисел порахувати: "))
b = 0
for i in range(n):
    b += a
    a += 5
print(b)

#9

a = 1000
n = int(input("Введіть кількість років: "))
for i in range(n):
    a *= 1.25
print(round(a, 2))

#10

a = int(input("Введіть ваше число: "))
factorial = 1
while a > 1:
    factorial *= a
    a -= 1
print(factorial)    