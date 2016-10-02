def cleanup(something):
    forbidden = ('!', '.', ',', '?', ':', ';', '-', '_', ' ', '...', '"', '\'')
    for char in forbidden:
        something = something.replace(char, "")
        # something_clean_lowercase = something_clean.lower()
    return(something.lower())


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)

something = str(input("Enter text: "))

clean = cleanup(something)

print(clean)

if is_palindrome(clean):
    print('Yes, it is a palindrome')
else:
    print('No, it is not a palindrome')
