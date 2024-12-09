print('#--------- set example -----------#')
s1 = {}
print (type(s1))    # <class 'dict'>
s1 = set()
print (type(s1))    # <class 'set'>
s1 = {50, 10, 10, 20, 30}
s1.add(10)
s1.add(10)
print(s1)           # {50, 10, 20, 30}
#print(s1[2:3])     # TypeError: 'set' object is not subscriptable
s1.remove(10)
print(s1)           # {50, 20, 30}
s2 = s1
print(s2)           # {50, 20, 30}
print(s1 is s2)
s2.add('false')
print(s1)           # {50, 20, 'false', 30}