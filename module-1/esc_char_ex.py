# -------------- Escape Characters (\) Example -----------------#

# Error Case
#print('Welcome to Python's online class') # SyntaxError: unterminated string literal

# Way - 1 - using escape character \ within the string
print('Welcome to Python\'s online class - 1')

# Way - 2 -- Adding single quote within double quote
print("Welcome to Python's online class - 2")

print("Python is a \"Programming\" Language")
print('Python is a "Scripting" Language')

print('Printing slash --> test\topic') # Printing slash --> test opic  --> slash got skipped
print('Printing slash --> test\\topic') # Printing slash --> test\topic

print('test \t topic') # test    topic  --> tab
print('test \n topic') # new line character 
print('test\b topic') # back space line character 
