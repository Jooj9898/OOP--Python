my_string = str(input("Enter a string:"))
encrypted_string = ""
for i, char in enumerate(my_string):
    encrypted_string += chr(ord(my_string[i]) + i)

print(encrypted_string)