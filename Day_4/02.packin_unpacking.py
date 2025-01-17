# %%
a = 10
b = 20

# %%
a = 10
b = 20

a = b
b = a 

print("a =", a)
print("b =", b)

# %%
a = 10
b = 20

a, b = b, a 

print("a =", a)
print("b =", b)

# %%
# Number of values different than numbers of variables

# %%
a, b = 10, 12, 30

# %%
a, b, c = 12, 30

# %%
a, *b, c = 10, 13, 15, 30, 45
print("a =", a)
print("b =", b)
print("c =", c)

# %%
a, b, *c = 10, 13, 15, 30, 45
print("a =", a)
print("b =", b)
print("c =", c)

# %%
def funct_with_params(first, second, *parameetres):
    print("parameteres = ", *parameetres, type(parameetres))

funct_with_params(2, 3, 243, 897, 654, 908, "polenta")

# %%
def funct_with_params(first, second, *args, **kargs):
    print("first", first, "second:", second)
    print("args:", args, type(args))
    print("kargs:", kargs, type(kargs))

funct_with_params(1,2, 3, 32, 4, generic="hello", dubai=30)

# %%
def funct_with_params(first, second, **kargs, *args):
    print("first", first, "second:", second)
    print("args:", args, type(args))
    print("kargs:", kargs, type(kargs))
