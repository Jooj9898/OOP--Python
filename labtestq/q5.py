user_input = str(input("Please enter some text:"))
string_els = user_input.split()
reversed_words = []
i = 0
for el in string_els:
    if i % 2 != 0:
        reversed_words.append(el[::-1])
    else:
        reversed_words.append(string_els[i])
    i+=1

new_str = " ".join(reversed_words)
print(new_str)
