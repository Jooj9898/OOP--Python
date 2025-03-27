my_list = ['xyzabc']
my_list.sort()
"".join(my_list)

print(my_list)

#reversing words#
my_str= "This is a test"
string_els = my_str.split()

reversed_els = []
for el in string_els:
    reversed_els.append(el[::-1])

new_str = " ".join(reversed_els)
print(new_str)