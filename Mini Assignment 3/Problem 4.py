keys = ["Ten", "Twenty", "Thirty"]
values = [10,20,30]
dict = {}

if(len(keys) != len(values)):
    print("Number of keys and values do not match")

for index in range(len(keys)):
    dict[keys[index]] = values[index]

print(dict)