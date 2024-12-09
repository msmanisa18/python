#----------------------- Type Casting to float -----------------------------#
#---- int to float -----#
a = 10          #--> int value
print(a)        # 10
print(type(a))  # <class 'int'>
b = float(a)    # Type Cast to float
print(b)        # 10.0
print(type(b))  # <class 'float'>

#---- complex to float -----#
a = 10 + 20j        # complex number
print(a)            # (10+20j)
print(type(a))      # <class 'complex'>
#b = float(a)       # Error, complex number cannot be converted to float
# TypeError: float() argument must be a string or a real number, not 'complex'

#---- bool to float -----#
a = True        #--> boolean value
print(a)        # True
print(type(a))  # <class 'bool'>
b = float(a)    # Type Cast to float
print(b)        # 1.0  # in case of False, the result will come 0.0
print(type(b))  # <class 'int'>

#---- str to float -----#
a = '10'        #--> str must be specified in base 10 format only
print(a)        # 10
print(type(a))  # <class 'str'>
b = float(a)    # Type Cast to float
print(b)        # 10.0
print(type(b))  # <class 'float'>

a = 'test'
#b = float(a)     # ValueError: could not convert string to float: 'test'
#print(b)

a = "20.9"
b = float(a)
print(b)        # 20.9








