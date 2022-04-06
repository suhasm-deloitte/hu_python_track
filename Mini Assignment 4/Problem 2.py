#Calculating total number of occurances of 'A' and 'a' using map() count() and lambda function

lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
result = list(map(lambda x: (x.count("a") + x.count("A")), lst1))
print(result)