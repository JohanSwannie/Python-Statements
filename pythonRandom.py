import random

# * RANDOM EXAMPLE 1 - random.choice()

def random1():
    my_list = ['apple', 'banana', 'orange', 'strawberry', 'mango']
    print(random.choice(my_list))
    
# random1()

# * RANDOM EXAMPLE 2 - random.randrange()

def random2():
    numbers = [12, 44, 13, 91, 57, 88, 34, 27]
    random_index = random.randrange(len(numbers))
    print(f"The random index is {random_index}")
    chosen_number = numbers[random_index]
    print(f"The random chose number is {chosen_number}")
    
# random2()

# * RANDOM EXAMPLE 3 - random.randint 1

def random3():
    numbers2 = [15, 25, 48, 7, 19, 94, 38, 22, 11, 45, 99]
    random_index2 = random.randint(0, len(numbers2) - 1)
    print(f"The random index is {random_index2}")
    chosen_number2 = numbers2[random_index2]
    print(f"The random chose number is {chosen_number2}")
    
# random3()

# * RANDOM EXAMPLE 4 - random.randint 2

def random4():
    randomList = []
    i = 1
    while i < 7:
        random_one = random.randint(1, 40)
        if random_one not in randomList:
            randomList.append(random_one)
            i+= 1
    randomList.sort()  
    print(f"The random numbers chosen for our lotto list are {randomList}")

# random4()

# * RANDOM EXAMPLE 5 - random with sample

def random5():
    from random import sample
    anotherList = [19, 33, 7, 81, 57, 20, 44]
    print(sample(anotherList, 3))

# random5()

# * RANDOM EXAMPLE 6 - random.shuffle

def random6():
    anotherList2 = [1, 2, 3, 4, 5]
    random.shuffle(anotherList2)
    print(anotherList2)

# random6()

