

def add(a,b):
    return a + b

def diff(a,b):
    return a - b

def do_operation(a, b, func):
    return func(a, b)

print(do_operation(30, 50, add))
print(do_operation(534, 50, diff))
