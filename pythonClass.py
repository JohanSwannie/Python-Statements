
# *  CLASS - EXAMPLE 1

class classOne:
    print('Hallo')
    
print(classOne)

# *  CLASS - EXAMPLE 2

class classTwo:
    b = 18; c = 7
    
value1 = classTwo();
print(f"value1 can be {value1.b} and value1 can be {value1.c}")

# *  CLASS - EXAMPLE 3

class Company:
  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age

person1 = Company("James", "Mower", 55)

print(person1.name)
print(person1.surname)
print(person1.age)

# *  CLASS - EXAMPLE 4

class Company2:
    def __init__(self, name2, surname2, age2):
        self.name2 = name2
        self.surname2 = surname2
        self.age2 = age2
        
    def __str__(self):
        return f"{self.name2} {self.surname2} is {self.age2}"

    def printThem(self):
        print(f"{self.name2} {self.surname2} is {self.age2} years old")

person2 = Company2("Luke", "Brown", 29)

print(person2)

person2.printThem()