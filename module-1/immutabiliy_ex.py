#--------------- Immutability Example -------------#

a = 10          
b = 10          
print(a)        #--> 10
print(b)        #--> 10
print(id(a))    #--> 140731292050504
print(id(b))    #--> 140731292050504
print(a is b)   #--> True
c = 10
print(id(c))    #--> 140731292050504