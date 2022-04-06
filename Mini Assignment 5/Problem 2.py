#Reduce function

from functools import reduce

#lst = [-1000, 500, -600, 700, 5000, -90000, -17500]
lst = [2, 3, 4, 6, 5]

print(reduce(lambda y, x: x*y, lst))