#----------------------- Type Casting to int -----------------------------#
#---- float to int -----#
a = 10.13       #--> floating point number
print(a)        # 10.13
print(type(a))  # <class 'float'>
b = int(a)      # Type Cast to int
print(b)        # 10
print(type(b))  # <class 'int'>

#---- complex to int -----#
a = 10 + 20j        # complex number
print(a)            # (10+20j)
print(type(a))      # <class 'complex'>
#b = int(a)         # Error, complex number cannot be converted to int
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

#---- bool to int -----#
a = True        #--> boolean value
print(a)        # True
print(type(a))  # <class 'bool'>
b = int(a)      # Type Cast to int
print(b)        # 1  # in case of False, the result will come 0
print(type(b))  # <class 'int'>

#---- str to int -----#
a = '10'        #--> str must be specified in base 10 format only
print(a)        # 10
print(type(a))  # <class 'str'>
b = int(a)      # Type Cast to int
print(b)        # 10
print(type(b))  # <class 'int'>

#a = 'test'
#b = int(a)     # ValueError: invalid literal for int() with base 10: 'test'
#print(b)

a = "20"
b = int(a)     
print(b)        # 20

#a = "20.9"
#b = int(a)     # ValueError: invalid literal for int() with base 10: '20.9'
#print(b)        


