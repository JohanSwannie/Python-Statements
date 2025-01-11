# * MATCH CASE - EXAMPLE 1

def match1():
    x = 90
    match x:
        case 50:
            print("You have failed the eaxams")
        case 90:
            print('You have scored very well')
        case _:
            print('Oops Koekoe')
    
# match1()
    

# * MATCH CASE - EXAMPLE 2

def match2(): 
    a = 4
    match (a == 1, a > 1):
        case (True, False):
            print('a is equal to 1')
        case (False, True):
            print('greater than 1')
        case _:
            print("Oops")
        
# match2()
        
# * MATCH CASE - EXAMPLE 3

def match3(x):
    match x:
        case 50 | 100 | 150 | 200: 
            print(f"Matched: {x}")
        case _:
            print("No match found")

# match3(50)
# match3(200)
# match3(150)
# match3(225)

# * MATCH CASE - EXAMPLE 4

def match4(input):
    match input:
        case [a, b]:  
            print(f"A correct list with 2 items: {a}, {b}")
        case [a, b, c]:  
            print(f"A correct list with 3 items: {a}, {b}, {c}")
        case (a, b, c, d, e):
            print(f"A correct tuple with 4 items: {a}, {b}, {c}, {d}, {e}")
                
        case _:
            print("Data Structure Unknown!")

# match4(['Cat', 'Dog'])
# match4(['Donkey', 'Horse', 'Mule'])
# match4(('BMW', 'Mercedes Benz', 'Toyota', 'Nissan', 'Volvo'))
# match4(['Chicken', 'Kangaroo', 'Pukeko', 'Elephant'])

# * MATCH CASE - EXAMPLE 5

def match5(person):
    match person:
        case {"name": name, "surname": surname}:  
            print(f"name: {name}, surname: {surname}")
        case {"name": name}:  
            print(f"name: {name}")
        case _:
            print("You must be kidding me - that is not a dictionary at all!")

# match5({"name": "Sona", "surname": "Kaur"})
# match5({"name": "Johan"})
# match5({'sport', 'Rugby'})
