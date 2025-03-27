def gcd(a,b):
    while b != 0:
        a, b = b, a %b
    return a
    
#function to add two fractions together
def add_fractions(fract1,fract2):
    if fract1[1] == fract2[1]:
        sum = ((fract1[0] + fract2[0]),fract1[1])
    else:
        LCM = (fract1[1] * fract2[1])/gcd(fract1[1],fract2[1])
        numerator1 = (fract1[0] *(LCM/fract1[1]))
        numerator2 = (fract2[0] *(LCM/fract2[1]))
        sum = (int((numerator1 + numerator2)),int(LCM))
    return sum

#function to multiply two fractions by each other
def multiply_fractions(fract1,fract2):
    return((fract1[0] * fract2[0]),(fract1[1] * fract2[1]))
    

add = add_fractions((7,8),(2,6))
multiply = multiply_fractions((1,6),(4,5))
print(add)
print(multiply)

