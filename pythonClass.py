
# *  CLASS - EXAMPLE 1

class classOne:
    print('Hallo')
    
print(classOne)

# *  CLASS - EXAMPLE 2

class classTwo:
    pass

employee1 = classTwo()
employee2 = classTwo()

employee1.fullName = "James Mower"
employee1.email = "james.mower@company1.com"
employee1.position = "Reporting Analyst"
employee1.salary = 85000

employee2.fullName = "Luke Brown"
employee2.email = "luke.brown@company1.com"
employee2.position = "Senior Data Analyst"
employee2.salary = 95000

print(f"Employee Name = {employee1.email} and Employee Salary = {employee1.salary}")
print(f"Employee Name = {employee2.email} and Employee Salary = {employee2.salary}")

# *  CLASS - EXAMPLE 3

class classThree:
    b = 18; c = 7
    
value1 = classThree();
print(f"value1 can be {value1.b} and value1 can be {value1.c}")

# *  CLASS - EXAMPLE 4

class Company:
  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age
    self.email = name + "." + surname + "@gmail.com"
    
  def fullName(self):
      return '{} {}'.format(self.name, self.surname)  

# * OR
  
#   def fullName(self):
#       return f"{self.name} {self.surname}"  

person1 = Company("James", "Mower", 55)

print(person1.name)
print(person1.surname)
print(person1.age)
print(person1.email)
print(f"Full Name of person is {person1.fullName()}")

# *  CLASS - EXAMPLE 5

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

print(Company2.printThem(person2))

# *  CLASS - EXAMPLE 6

class Employees:
    
    employees_total = 0
    raisePercentage = 1.08
    
    def __init__(self, first, last, payment):
        self.first = first
        self.last = last
        self.payment = payment
        Employees.employees_total += 1
        
    def paymentRaise(self):
        self.payment = int(self.payment * self.raisePercentage)


emp1 = Employees("Mary", "Callahan", 55000)
emp2 = Employees("Danny", "Black", 70000)

print(f"Total of employees = {Employees.employees_total}")

print(f"Employees Dictionary = {Employees.__dict__}")
print("-----------------------------------------------------------------------------------------------------------")
print(f"Employee One Dictionary = {emp1.__dict__}")
print("-----------------------------------------------------------------------------------------------------------")
print(f"Employee Two Dictionar = {emp2.__dict__}")
print("-----------------------------------------------------------------------------------------------------------")

print(f"The employee's salary before a raise is {emp1.payment}")

emp1.paymentRaise()

print(f"The employee's salary after a raise is {emp1.payment}")

# *  CLASS - EXAMPLE 7

class Employees2:
    
    raisePercentage2 = 1.08
    
    def __init__(self, fullName, salary):
        self.fullName = fullName
        self.salary = salary
        
    @classmethod
    def salaryRaise(cls, amount):
        cls.raisePercentage2 = amount
        
    @classmethod
    def createObjects(cls, string):
        fullName, salary = string.split('-')
        return cls(fullName, salary)
        
empl1_string = "Gary Handover-88000"
empl2_string = "Natasha Goodman-95000"

empl1 = Employees2.createObjects(empl1_string)
empl2 = Employees2.createObjects(empl2_string)

Employees2.salaryRaise(1.10)

print(f"Employees raise percentage = {Employees2.raisePercentage2}")
print(f"Employee One raise percentage = {empl1.raisePercentage2}")
print(f"Employee Two raise percentage = {empl2.raisePercentage2}")
    

    



