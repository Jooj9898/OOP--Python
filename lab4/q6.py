my_str = "Susie Perkins"
reverse_str = ""
length = len(my_str) -1
index = 0

while length>= 0:
    reverse_str += my_str[length]
    length = length -1 

print(reverse_str)

