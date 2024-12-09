#---------------- tuple example -------------#
print ('#------------ tuple example ---------#')
t1 = ()             # Empty tuple
t2 = (10)
print(type(t1))     # <class 'tuple'>
print(type(t2))     # <class 'int'>
t3 = (10,)
print(type(t3))     # <class 'tuple'>
t4 = (10, 20, 30,)
print(type(t4))     # <class 'tuple'>
t5 = (10, 20, 30)
print(type(t5))     # <class 'tuple'>
t6 = t5
print(id(t5))
print(id(t6))
print(t5 == t6)
print(t5 is t6)
print(t4 is t5)
print(t4[-1])
print(t4[1])
print(t4[0:2])

