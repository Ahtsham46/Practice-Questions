def check_palindrome(s):
    s = s.replace(" ", "").lower()
    new = s[::-1]
    if new == s:
        print("It is palindrome.")
    else:
        print("It is not palindrome.")
    return 0
string = "A man a plan a canal Panama"

print(check_palindrome(string))