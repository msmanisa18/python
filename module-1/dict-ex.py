print('#------------ dict example -------------#')
d1 = {}
print(d1)           # {}

d2 = {101:'Ramesh', 102:'Suresh', 103:'Gopal'}
print(d2)           # {101: 'Ramesh', 102: 'Suresh', 103: 'Gopal'}
d2[101] = 'Hari'
print(d2)           # {101: 'Hari', 102: 'Suresh', 103: 'Gopal'}

d2.update({104:'Test User'})
print(d2)           # {101: 'Hari', 102: 'Suresh', 103: 'Gopal', 104: 'Test User'}

del d2[101]
print(d2)           # {102: 'Suresh', 103: 'Gopal', 104: 'Test User'}