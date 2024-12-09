#----------------------- Type Casting to complex -----------------------------#
#---- int to complex -----#
a = 10          	    # int value
print(complex(a))       # (10+0j)
b = 20
print(complex(a, b))    # (10+20j)

#---- float to complex -----#
a = 10.23          	    # float value
print(complex(a))       # (10.23+0j)
b = 20.094
print(complex(a, b))    # (10+20.094j)

#---- bool to complex -----#
a = False         	    # bool value
print(complex(a))       # (0j)
a = True  
b = True
print(complex(a, b))    # (1+1j)

#---- str to complex -----#
a = '10.5'         	    # str value
print(complex(a))       # (10.5+0j)
#b = '20.4'
#print(complex(a, b))   
# TypeError: complex() can't take second arg if first is a string

a = 10.5
b = '20.4'
#print(complex(a, b)) #TypeError: complex() second arg can't be a string





