#2. Palindrome Checker Write a program that checks if a given word is a palindrome.

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
# Example usage
word = "madam"
if is_palindrome(word)==True:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
