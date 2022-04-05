list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
final_list = list()

for str1 in list1:
    for str2 in list2:
        final_list.append(str1 + str2)

print(final_list)