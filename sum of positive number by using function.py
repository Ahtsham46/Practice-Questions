num = [1, 5, 7, -3, 5, -9, 4]
def summ_positive(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total
            
print(summ_positive(num))


