# program runs way to long need to figure out a more efficient way to solve.

number = 600851475143
factor = 600851475142

while(number > 0):
    if number%factor == 0:
        break
    else:
        factor -= 1
        print(factor)
        

print(factor)
