# Input number
number = int(input("Enter a number: "))
# Initialize the sum
sum_of_digits = 0
# Calculate the sum of the digits
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number = number // 10
#result
print(f"Sum of the digits is: {sum_of_digits}")
