def selection_sort(arr):
    for i in range(len(arr) -1):
        min = i
        for j in range(i + 1, len((arr))):
            if float(arr[j][1]) % 1 < float(arr[min][1]) % 1:

                min = j
        if min != i:
            temp = arr[min]
            arr[min] = arr[i]
            arr[i] = temp
sample_data = [('item1', '12.20'), ('item2','15.10'), ('item3','24.5')]
selection_sort(sample_data)

print(sorted(sample_data[0][1]))
outcome =[]
for el in sample_data:
    outcome.append(list(el))
for el in outcome:
    print("HI")