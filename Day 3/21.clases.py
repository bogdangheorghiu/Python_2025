

# class -> keyword
# convention -> class names are Capitalize
class Cat:
    ## __init__ -> initialiser
    ## self -> refernce to the current object
    def __init__(self, name, age):
        ## self.name - the object has an attribut called name
        self.name = name
        self.age = age

    def __str__(self):
        return f"The cat {self.name} has {self.age} yers."


## Creating objects
cat_objects1 = Cat("Rino", 5.5)
print(cat_objects1)
print(cat_objects1.name)
print(cat_objects1.age)
print(type(cat_objects1))

a_string = str(cat_objects1)
print("Converted string:", a_string)
 
#cat_objects2 = Cat("Pierre", 7.5)
#print(cat_objects2.name)
#print(cat_objects2.age)