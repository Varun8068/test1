def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
n = 10
fact = factorial(n)
print(f"The factorial of {n} is:", fact)

