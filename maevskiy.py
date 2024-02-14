import math
x = float(input("Введіть x: "))
summ = 0
for k in range(1, 73):
    summ += (pow(-1, k) * pow(x, 3 * k-1)) / (math.factorial(2 * k + 1))
print(round(summ, 2))    