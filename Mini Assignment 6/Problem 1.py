# Decorator which will execute the function twice

def decorator(func):
    def repeat(num1, num2):
        func(num1, num2)
        func(num1, num2)

    return repeat


@decorator
def multiply(num1, num2):
    print(num1 * num2)


multiply(2, 3)