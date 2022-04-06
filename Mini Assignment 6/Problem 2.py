# Generator to return the fibonnaci sequence starting from
# the first element up to (n).

def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

n = int(input("Enter the limit : "))
x = fib(n)

for i in x:
    print(i, end=' ')