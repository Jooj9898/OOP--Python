my_dict = {'a':15, 'c':35, 'b':20}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

for key, value in sorted(my_dict.items()):
    print(key,value)
for value,key in sorted(my_dict.items()):
    print(value,key)