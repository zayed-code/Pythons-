a = "ZAYED"
t = type(a) # cllass <int>
print(t)

a = "31.2"
t = type(a) # class <int>
print(t)

a = "31.2"
a = float(a) # convert string to float # a but the type should be float
t = type(a) # class <float>
print(t)    