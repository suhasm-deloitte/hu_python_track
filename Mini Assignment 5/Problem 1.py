#Printing the numbers which are converted from negative to positive

lis1 = [-1000, 500, -600, 700, 5000, -90000, -17500]

result = list(filter(lambda x : x, map(lambda x: -x if x < 0 else None, lis1)))

print(result)