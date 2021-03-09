## Write a program that asks a user for a string
# and check if the string is a palindrome

def check_palindrome(word):
    """
    Given a word, check if it is a palindrome.
    A palindrome is a word that reads the same backward and forward

    >>> check_palindrome("racecar")
    True
    >>> check_palindrome("rotator")
    True
    >>> check_palindrom("word")
    False
    """

    pass



user_input = input("Enter a word and I will check if it is a palindrome: ")

is_palindrome = check_palindrome(user_input)

if is_palindrome:
    print("The word you chose is a palindrome!")
else:
    print("This word is not a palindrome")