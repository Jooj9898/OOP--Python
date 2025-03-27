#Practice 6

"""
skiiiip
"""

#Practice 7
arr = []
divisor = 17

for i in range(100, 999):
    if i % 17 == 0:
        arr.append(i)

print("3 digit mulitples of 17:\n", arr)
print("Number of multiples: ", len(arr))

#Practice 8
# (a)
x = int(input("Enter number: "))
i = 0
result = 0
i2 = 0
result2 = []


while i < x:
    i += 1
    result += i
    result2.append(result)

print("Result: ", result)
print("Results:\n", result2)

# (b) have to do in a different loop within a loop okay 
