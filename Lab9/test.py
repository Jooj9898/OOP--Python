def get_tuple(string):
    new_string = string.split(' ')
    return tuple(new_string)
test_string = "car 5000"
test_string2 = "table 100"

products = [get_tuple(test_string)]
products = products + [get_tuple(test_string2)]
print(products)
