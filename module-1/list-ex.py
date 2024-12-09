#------ Python - list data type example  --------#

#To represent an empty list in Python, use []
l1 = []
print(type(l1))              # <class 'list'>

# add elements to the list
l1.append('Alok')
l1.append('Surya')
print(l1)                    # ['Alok', 'Surya']

#l1.append('Papu', 'Asish')  # TypeError: list.append() takes exactly one argument (2 given)
#print(l1)

# Duplicate elements are allowed, insertion order preserved
l1.append('Alok')
l1.append('Surya')
print(l1)                    # ['Alok', 'Surya', 'Alok', 'Surya']

# Removing elements from list
l1.remove(l1[1])
print(l1)                    # ['Alok', 'Alok', 'Surya']
l1.remove('Alok')
print(l1)                    # ['Alok', 'Surya']

# Adding heterogeneous elements is possible
l1.append(10+20j)
l1.append(10)
l1.append(True)
l1.append(20.45)
print(l1)                    # ['Alok', 'Surya', (10+20j), 10, True, 20.45]

l2 = [10, 20, 30, 40, 10, 20, 30.5, True, 'True']
print('------------------- Printing l2 -------------------')
print(l2)
print(l2[0])    # 10
print(l2[-1])   # True
l2.remove(10)
print(l2)       # [20, 30, 40, 10, 20, 30.5, True, 'True']
print(l2[2:6])  # [40, 10, 20, 30.5]  --> prints from 2nd to till 6th element not the 6th element

print('------------------- list comparison -----------------')
list1 = [1, 3, 2, 4, 5]     # single = symbol is called as assignment operator
list2 = [1, 3, 2, 4, 5]
print(list1 == list2)       # double == symbol is called as comparison operator, here it compares value
print(list1 is list2)       # here it compares address
print(id(list1))
print(id(list2))

print('------------------- list assignment -----------------')
list3 = list1
print(list1 == list3)
print(list1 is list3)
print(id(list1))
print(id(list3))
print(list1[3])
print(list3[3])
list3[3] = True
print('------------------- after assignment -----------------')
print(list1[3])
print(list3[3])
print('------------------- after assignment2 -----------------')
list2[3] = False
print(list1[3])
print(list2[3])
print(list3[3])
