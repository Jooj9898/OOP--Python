user_input = int(input("Enter a number:"))

if user_input < 10:
    print("not a kaprekar number")
else:
    sum = 0
    squared_number = user_input ** 2
    squared_number = str(squared_number)
    first_half = ""
    second_half = ""
    mid = len(str(user_input))//2
    first_half = first_half + squared_number[:mid + 1]
    second_half = second_half + squared_number[mid + 1:]
    print("first half =", first_half)
    print("second half =", second_half)
    sum = int(first_half) + int(second_half)
    if sum == user_input:
        print("input is kaprekar num")
    else:
        print("not kaprekar")

