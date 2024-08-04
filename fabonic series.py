def fibonacci_series(n):
    fib_series = [0, 1]
    while True:
        next_number = fib_series[-1] + fib_series[-2]
        if next_number > n:
            break
        fib_series.append(next_number)
    return fib_series
n = int(input("Enter a number: "))
result = fibonacci_series(n)

print(f"Fibonacci series up to {n}: {result}")
