#--------------bytes example ----------#

l = [10, 20, 30, 10, 20, 30, 40, 30]
b = bytes(l)
print(type(b))      # <class 'bytes'>
for x in b:
	print(x)
#b[1] = 200         # TypeError: 'bytes' object does not support item assignment

#-------- bytearray example ----------#
ba = bytearray(l)
print(type(ba))     # <class 'bytearray'>
ba[1] = 200
for x in ba:
	print(x)