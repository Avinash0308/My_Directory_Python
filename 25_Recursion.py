def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
print(factorial(15))
print(factorial(25))
print(factorial(35))

# program to print the fibonacci series
def fibonacci(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(15))