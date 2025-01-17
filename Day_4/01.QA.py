# %%
a_b_c = 10_000_000
a_b_c, type(a_b_c)

# %%
a_b_c = 10,000,000
a_b_c, type(a_b_c)

# %%
"""
# Packing and Unpacking
"""

# %%
a,b,c = 1000, 2000, 3000
print(a)

# %%
x, y = (10,2)
print("x =", y)
print('y =', x)

# %%
import math as mathematics
mathematics.pi


# %%
int("19")

# %%
a = {1, 2, 3}
print(a, type(a))

# %%
"""
#Possible but not preffered 
"""

# %%
a = dict(x=2)
a

# %%
"""
# prefered way to defining a dictionary
"""

# %%
a = {"x":2}
a

# %%
johanis = {"cars":2, "houses":6}
johanis["cars"] = 3
print(johanis)

# %%
x = {[]:"hello"}
print(bool(x))

# %%
x = {0: None}
print(bool(x))

# %%
x = {None : None}
print(bool(x))

# %%
x = "Kill two birds with one stone"
print(x[4:-1])

# %%
x, y, z = 0, 1, 0

print("x=", x)

# %%
letters = ["a", "b", "a", "v", "g", "n"]    
ch = "a"
indexes = [ i for i in range(len(letters)) if letters[i] == ch]
indexes