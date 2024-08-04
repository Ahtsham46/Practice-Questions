def factorial(n):
    
    fact = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n+1):
            fact *= i
        return fact
number = 4
print(factorial(number))