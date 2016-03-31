def cleanup(something):
    forbidden = ('!', '.', ',', '?', ':', ';', '-', '_', ' ', '...', '"', '\'')
    for char in forbidden:
        something = something.replace(char, "")




# def reverse(text):
#     return text[::-1]


# def is_palindrome(text):
#     return text == reverse(text)

something = str(input("Enter text: "))


# if is_palindrome(something):
#     print('Yes, it is a palindrome')
# else:
#     print('No, it is not a palindrome')
