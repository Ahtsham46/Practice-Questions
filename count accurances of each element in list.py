def count_occurrences(elements):
    counts = {}
    for element in elements:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts

# Example usage
elements = ["apple", "banana", "apple", "cherry", "banana", ]
counts = count_occurrences(elements)

for element, count in counts.items():
    print(f"{element}: {count}")
