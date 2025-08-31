#'type' function is used to find the datatype of the given variable.

a = 123
print (type(a)) # class 'integer or int'

b = 43.8
print (type(b)) # class 'float'

c = "Python"
print (type(c)) # class 'string or str'

d = False
print (type(d)) # class ' boolean or bool'

e = None
print (type(e)) # class ' NoneType'

#Datatype conversions
a = "31.2" # anything under a double quote in python is a "string"
b =  float(a)
c = type (b)
print (c) # so the class is converted to float from string.

a = 78.9
b = int(a)
c = type (b)
print (c) # class converted to string from float.