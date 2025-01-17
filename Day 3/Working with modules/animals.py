


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years"
    


class Dog(Animal):
    def bark(self):
        print("uf uf") * self.age



print(animal_obj)

class HungariaDog(Animal):
    def bark(self):
        print("vau" * self.age)


class RomaninaDog(Animal):
    def bark(self):
        print("ham" * self.age)

       
animal_obj = Animal("Boy", 3)     
       
dog_obj = RomaninaDog("Spike", 10)
print(dog_obj)