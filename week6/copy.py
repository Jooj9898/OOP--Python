a_list = [1,2,3]
b_list = [5,6,7]
a_list.append(b_list)
a_list = [1,2,3,[5,6,7]]

import copy
c_list = copy.deepcopy(a_list)

b_list[0] = 1000
a_list  [1,2,3,[1000,6,7]]
c_list  [1,2,3,[5,6,7]]

##example:
ListA = [1,2,3,4,5]
ListB = []
for num in ListA:
   ListB.append(num)
ListA[2] = 10

#Initial schedules
employee_schedules = {
    'Alice': ['Meeting', 'Code Review', 'Write Report'],
    'Bob': ['Design Meeting', 'Write Code'],
    'Charlie': ['Test Code', 'Fix Bugs']
}

# Create a backup using deep copy
backup_schedules = employee_schedules

# Update original schedules
employee_schedules['Alice'].append('Team Lunch')
employee_schedules['Bob'][0] = 'Client Meeting'

# Check schedules
print("Original schedules:", employee_schedules)
print("Backup schedules:", backup_schedules)



# Initial seating arrangements
classrooms = [['Alice', 'Bob', 'Charlie', 'David'], ['Eve', 'Frank', 'Grace', 'Heidi']]

# Create a backup using shallow copy
backup_classrooms = classrooms[:]

# Update seating arrangements
classrooms[0][1] = 'Zoe'  # Change 'Bob' to 'Zoe'
classrooms[1].append('Ivan')  # Add 'Ivan' to the second row 


# Check seating arrangements
print("Original seating arrangements:", classrooms)
print("Backup seating arrangements:", backup_classrooms)




