string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count = count + 1
print("Total number of vowels in string: ", count)