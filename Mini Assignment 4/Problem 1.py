#calculating the equation "ax^2+bx+c" using lambda function

result = lambda a, b, c, x: (a * (x ^ 2)) + (b * x) + c
print(result(1, 2, 3, 4))