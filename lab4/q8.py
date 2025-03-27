code = str(input(("Enter a code:")))
encrypted_code = ""
length = len(code)
index = 0

for char in code:
    encrypted_code += chr((ord(char) + 1))

print(encrypted_code)


