d1 = {'a':100, 'b':200,'c':300}
d2 = {'a':300,'b':200, 'd':400}
d3 = {}
d3['new_key'] = 'new_value'

for key,value in d1,d2.items():
    if key == key:
        new_value = value + value
        d3 = {key,new_value}
print(d3)