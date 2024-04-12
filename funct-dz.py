import math
import random

#1

def size_of_cone():
    radius = float(input("Введіть радіус конуса: "))
    height = float(input("Введіть висоту конуса: "))

    volume = round((1/3) * math.pi * radius ** 2 * height, 2)
    print("Об'єм конуса: ", volume)
size_of_cone()

#2

def area_of_right_triangle(base, height):
    return 0.5 * base * height

def area_of_circle(radius):
    return math.pi * radius ** 2

base1 = 5
height1 = 8

base2 = 3
height2 = 6

radius = 4

area_triangle1 = area_of_right_triangle(base1, height1)
area_triangle2 = area_of_right_triangle(base2, height2)

area_circle = area_of_circle(radius)

print("Площа першого прямокутного трикутника:", round(area_triangle1, 2))
print("Площа другого прямокутного трикутника:", round(area_triangle2, 2))
print("Площа кола:", round(area_circle, 2))

#3

def average(nums):
    return sum(nums) / len(nums)

def roll_dice():
    return random.randint(1, 6)

results = []

for _ in range(5):
    results.append(roll_dice())

avg_result = average(results)

print("Результати підкидання кубика:", results)
print("Середнє значення результатів:", avg_result)

#4

def calculate_expression(a, b, c, d):
    return a * b - c / d

list_values = [3, 5, 2, 7]

tuple_values = (4, 1, 5, 6)

result_list = calculate_expression(*list_values)

result_tuple = calculate_expression(*tuple_values)

print("Значення виразу для списку:", round(result_list, 2))
print("Значення виразу для кортежу:", round(result_tuple, 2))

#5

def sum_of_squares(num1, num2, num3):
    return num1 ** 2 + num2 ** 2 + num3 ** 2

random_numbers = [random.randint(3, 7) for _ in range(3)]

print("Випадкові числа:", random_numbers)

result = sum_of_squares(*random_numbers)

print("Сума квадратів випадкових чисел:", result)

#6

def average(nums):
    return sum(nums) / len(nums)

def calculate_areas(regions):
    areas = list(regions.values())
    max_area = max(areas)
    min_area = min(areas)
    avg_area = average(areas)
    return max_area, min_area, avg_area

regions = {
    "Чернігівська область": 31802,
    "Київська область": 28131,
    "Черкаська область": 20903,
    "Кіровоградська область": 24587,
    "Дніпровська область": 31911,
    "Запорізька область": 27213,
    "Херсонська область": 28491,
    "Миколаївська область": 24590,
    "Полтавська область": 28745,
    "Сумська область": 23866,
    "Вінницька область": 26514
}

# Обчислення середньої площі
max_area, min_area, avg_area = calculate_areas(regions)

# Виведення результатів
print("Максимальна площа:", max_area)
print("Мінімальна площа:", min_area)
print("Середня площа:", round(avg_area, 2))