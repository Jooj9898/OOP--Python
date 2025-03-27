import string

original_str = input("Input a string: ")
modified_str = original_str.lower()
reverse_str = ""
length = len(modified_str) - 1

bad_chars = string.whitespace + string.punctuation

modified_str = modified_str.replace(bad_chars,"" )

while length >= 0:
    reverse_str += modified_str[length]
    length = length -1

if reverse_str == modified_str:
    print("this is a palindrome")
else:
    print("this is not a palindrome")



