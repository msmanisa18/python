#------- Type Casting to bool ---#

#---- int to bool -----#
print('---- int to bool -----')
a = 10          	# int value
print(bool(a))      # True 
a = -20          	# int value
print(bool(a))      # True 
a = 0            	# int value
print(bool(a))      # False 
# zero --> False, non zero --> true

#---- float to bool -----#
print('---- float to bool -----')
a = 10.4          	# float value
print(bool(a))      # True 
a = -20.5          	# float value
print(bool(a))      # True 
a = 0.0            	# float value
print(bool(a))      # False 
# zero --> False, non zero --> true

#---- complex to bool -----#
print('---- complex to bool -----')
a = 10.4+1j         # complex value
print(bool(a))      # True 
a = -20.5+2j        # complex value
print(bool(a))      # True 
a = 0+0j            # complex value
print(bool(a))      # False 
# zero --> False, non zero --> true

#---- str to bool -----#
print('---- str to bool -----')
a = 'test data'     # str value
print(bool(a))      # True 
a = ''              # str value
print(bool(a))      # False 
# empty string --> False, non empty string --> True
a = '     '         # str value
print(bool(a))      # True 





