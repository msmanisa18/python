#-------------- Python range Example ---------------#

print('#-------- 1. Create a sequence of numbers from 0 to 5 -------#')
r = range(6)
print(r)

# Display the output of range using a for loop
for x in r:
    print(x)

print('#------- 2. Create a sequence of numbers from 10 to 15 ------#')
r = range(10, 16)
for x in r:
    print(x)

print('#------ 3. Create a sequence of numbers from -10 to -15 -----#')
r = range(-15, -9)
for x in r:
    print(x)

print('#------ 4. Display all even numbers from 1 to 20 -----#')
r = range(2, 21, 2)
for x in r:
    print(x)

print('#------ 5. Use of slice operator in range -----#')
s = r[2:5]
for x in s:
    print(x)

print('#------ 4. Display all even numbers from 21 to 2 -----#')
r = range(21, 2, -2)
for x in r:
    print(x)
