# a modulo n (often abbreviated as a mod n) is the remainder of the Euclidean division of a by n, where a is the dividend and n is divisor
def modulo_operation(dividend, divisor):
    if dividend % divisor == 0:
        print(str(dividend)+" is multiple of "+str(divisor))
    else:
        remainder = dividend % divisor
        print(str(dividend)+" % "+str(divisor)+", the remainder is "+str(remainder))

modulo_operation(5,2)
modulo_operation(4,2)
modulo_operation(9,3)
modulo_operation(81,9)
modulo_operation(72,5)

'''
The range of values for an integer modulo operation of n is 0 to n − 1 inclusive (a mod 1 is always 0; a mod 0 is undefined, 
possibly resulting in a division by zero error in some programming languages)
'''