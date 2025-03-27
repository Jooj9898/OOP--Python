print([n**2 for n in range(1,101)])
print([n.upper() for n in ['Red','Blue','Green','Black','White']])
print([n for n in range(1,1001) if n % 7 ==0])
print([n for n in range(1,101) if '3' in str(n)])
print(len([n for n in 'Hey there are you for real' if n == ' ']))
print("".join([n for n in 'Hey there are you for real' if n not in 'aeiou']))
print(" ".join([n for n in 'Hey there are you for real'.split() if len(n) < 4]))
print([n for n in range(1, 1001) if True in [True for i in range(2,10) if n % i == 0]])
    