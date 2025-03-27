

def get_tuple(user_input):
    user_input = user_input.split()
    user_input = tuple(user_input)
    print(user_input)

def menu(file_to_open):
    file_to_open = input("Open what file:")
    input("Please enter two movies as 'name (year)' separated by the appropriate operator (&, |, -), or enter "'.'" to quit:")
    print("the set of actors for this operation is:")

my_dict = {}
my_file = open("C:\Users\mcgar\OneDrive\Desktop\OOP\lab 8\movies.txt")
my_file = get_tuple(my_file)    
my_dict[my_file] = my_file
print(my_dict)   
