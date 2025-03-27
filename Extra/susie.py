#susie susie susie
"""
print("hello world!")

#Practice 1
grade = int(input("Enter mark between 0 and 100: "))

if grade >= 40:
    print("This is a pass")
else:
    print("This is a fail")

#Practice 2
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 < num2:
    print("Number 1 is smaller than number 2")
elif num1 > num2:
    print("Number 1 is larger than number 2")
else:
    print("Number 1 is equal to number 2")

#Practice 3
n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))
operation = input("Enter operation (+, -, *, /): ")
result = 0

if operation == '+':
    result = n1 + n2

elif operation == '-':
    result = n1 - n2

elif operation == '*':
    result = n1 * n2

elif operation == '/':
    result = n1 / n2
else:
    print("Invalid input")

print("Result =", result)


#Practice 4
N1 = int(input("Enter number: "))
N2 = int(input("Enter number: "))
N3 = int(input("Enter number: "))

if N1 > N2 and N1 > N3:
    print(N1, "is largest")
elif N2 > N1 and N2 > N3:
    print(N2, "is largest")
elif N3 > N1 and N3 > N2:
    print(N3, "is largest")
else:
    print("The largest value is tied")


#Practice 5
user_str = input("Enter a positive integer:") # Line 1
my_int = int(user_str)
count = 0
while my_int > 0:
   if my_int % 2 == 1:
       my_int = my_int//2
   else:
       my_int = my_int - 1
   count += 1 # Line 2
print(count) # Line 3
print(my_int) # Line 4


#(A)= 4
#(B)= 0
#(C) type associated with line one? string?
#(D) count become count plus one
#(E) colon in necessary syntax of while
"""

#Practice 6