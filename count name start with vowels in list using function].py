def count_name(names):
    vowels = "aeiouAEIOU"
    total = 0
    for name in names:
        if name[0] in vowels:
            total += 1
    return total

names = ["ALi", "Sameer", "Saba", "Noor", "Ayesha"]
print(count_name(names))
