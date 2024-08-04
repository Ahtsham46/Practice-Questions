# Function to count total words and lines in a text file
def count_words_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        total_lines = len(lines)
        total_words = sum(len(line.split()) for line in lines)
    return total_words, total_lines

file_path = 'practice.txt'  

total_words, total_lines = count_words_lines(file_path)

print(f"Total number of words: {total_words}")
print(f"Total number of lines: {total_lines}")
