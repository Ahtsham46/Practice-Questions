def even_odd(n):
    if n % 2 == 0:
        return f"{n} is Even."
    else:
        return f"{n} is Odd."
number = 4
print(even_odd(number))