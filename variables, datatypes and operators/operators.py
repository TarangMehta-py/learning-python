# Arithmetic Operators
a = 134
b = 252
c = a+b

print (c)

# Assignment Operators
a = 16-5 # assign 4-2 in a
print (a)

b =  64
b += 6 # increment the value of b by 6 and then assign it to b, can do same with subtraction(-/), multiplication(*/) and division(/=)
print (b)

c = a+b 
print (c)

# Comparison Operators; gives only boolean outputs.

a = 5<4
print (a) # output = False
b =  5>4
print (b) # output = True
c = 5>5 # output = False
#but
d = 5>=5
print (d)

e = 5!=5
print (e) # output = False, != is the not equal to sign.

f = 5==5
print (f)# output = True

# Logical operators
a = True or False
print (a) # output = True, why?

#python truth table for 'or'

"""1- True or False is true
   2- False or true is true
   3- True or True is True
   4- False or False is False"""

# python truth table for 'and'

"""1- True and False is False
   2- False and true is False
   3- True and True is True
   4- False and False is False"""

#'not' changes the true and false output. 
print (not(False))
print (not(True))