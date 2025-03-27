name = "susie"
target = input("Input a target to find: ")

for index in range(len(name)):
   if name[index] == target:
       print("Letter found at index", index)
       break
else:
   print("Letter", target, "not found in river", name)
