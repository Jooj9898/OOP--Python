arr = []
divisor = 17

for i in range(100, 999):
    if i % 17 == 0:
        arr.append(i)

print("3 digit mulitples of 17:\n", arr)
print("Number of multiples: ", len(arr))




