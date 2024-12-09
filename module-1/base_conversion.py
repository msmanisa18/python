#--------------- Base Conversion Example -------------#

a = 15666
print(a)        #--> 15666, prints in default Format, which is Decimal
print(bin(a))   #--> 0b11110100110010 --> Prints in Binary Format
print(oct(a))   #--> 0o36462 --> Prints in Octal Format
print(hex(a))   #--> 0x3d32 --> Prints in Hexa Decimal Format

a = 0x3d32
print(bin(a))   #--> 0b11110100110010
print(oct(a))   #--> 0o36462
print(a)        #--> 15666