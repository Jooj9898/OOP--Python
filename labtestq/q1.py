def sum_divisors(my_num):
    if user_input > 0:
        sum = 0
        for i in range (1,my_num + 1):
            if my_num % i == 0:
                sum += i
        print("sum =",sum)
    else:
        print("cannot take a negative")
user_input = int(input("Please enter a number:"))
sum_divisors(user_input)

# Lucas solution:
def sum_divisors(number: int) -> None:
    """Find the sum of all divisors from 1 up to number"""

    if number < 0:
        print("Negative number only positive numbers accepted")
    
    sum = 0
    equation = ""
    for i in range(1, number + 1):
        if number % i ==0:
            sum += i
            equation += str(i) + "+"
    
    equation = equation[:-3] + " = " + str(sum)
    
    print(equation)