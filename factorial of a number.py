num = int(input("Enter a number for factorial: "))
fact = 1
for n in range(1,num+1):
    fact *= n
print(f"Factorial of a number is: {fact}")