import math
x=5.3
k=3
a = math.log(abs(x))
b = pow(math.e, k) + a
y = pow(a, 2)+pow(b, 2)
print(round(y,2))