# To find the longest  word in the text file

with open("a.txt", "r") as file:
    lst = file.read().split()

print(max(lst, key=len))