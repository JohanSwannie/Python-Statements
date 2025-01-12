
# * DELETE STATEMENT - EXAMPLE 1

def delOne():
    a = 18; b = 7; c = 22
    del a
    try:
        print(a)
    except NameError:
        print('Variable "a" is now deleted and can not be accessed')
    else:
        print(f'Variable "a" still exists and is {a}')
    finally:
        print("Test completed")
        print(f'If variables "b" and "c" still exist, then "b" is {b} and "c" is {c}')
    
# delOne()

# * DELETE STATEMENT - EXAMPLE 2

def delTwo(dict):
    del dict["age"]
    print(f"dict should now be without the age {dict}")
    
dict1 = {"name": "Billy", "surname": "Brown", "age": 28}

# delTwo(dict1)

# * DELETE STATEMENT - EXAMPLE 3

def delThree(list):
    while True:
        try:
            idx = list.index('Cat')
        except ValueError:
            print('Value error occured and therefore we will break out of the loop')
            break
        else:
            del list[idx]
        print(f"The values remaining in the list are now {list}")
    
list1 = ['Chicken', 'Cat', 'Dog', 'Horse', 'Cat', 'Chicken', 'Cat', 'Turkey']

delThree(list1)