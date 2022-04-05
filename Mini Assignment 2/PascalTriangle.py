n = int(input("Enter value of n: "))

for i in range(n):
    print(11 ** i, end="")
    for j in range(n - i - 1):
        print(0, end="")
    print()