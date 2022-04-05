dict = {'name': "Kelly",
              'age': 25,
              'salary': 8000,
              'city': "New york"
        }

print("Initial Dictionary: ", dict)

dict['Location'] = dict.pop('city')
print("Final Dictionary: ", str(dict))