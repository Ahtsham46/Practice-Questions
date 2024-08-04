def reverse(sentence):
    word = sentence.split()
    reverse_word = word[::-1]
    reverse_word = " ".join(reverse_word)
    return reverse_word
sentence = "Ali is good but why late from school"
print(reverse(sentence))