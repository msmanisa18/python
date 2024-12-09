print('#--------- frozenset example -----------#')
s = {10, 20, 20, 10}
fs = frozenset(s)
print(fs)               # frozenset({10, 20})

print('#------ 1. empty frozenset example -----#')
fs1 = frozenset({})
print(fs1)              # frozenset()

print('#------ 2. empty frozenset example -----#')
s2 = set()
fs2 = frozenset(s2)
print(fs2)              # frozenset()