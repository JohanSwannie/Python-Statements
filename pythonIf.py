    
# * IF STATEMENT - EXAMPLE 1

lista = [5, 10, 15]

def ifOne(a):
    if a < 10:
        print(f"a is smaller than 10 because a = {a}")
    elif a > 10:
        print(f"a is bigger than 10 because a = {a}")
    else:
        print(f"a is equal than 10 because a = {a}")
    
# for i in range(len(lista)):
#     ifOne(lista[i]) 
    
# * IF STATEMENT - EXAMPLE 2

Andy = 22; Mary = 27; Billy = 19

def ifTwo():
    if ((Andy > Mary) and (Andy > Billy)):
        print(f"Andy is the oldest at {Andy} years old")
    elif ((Mary > Andy) and (Mary > Billy)):
        print(f"Mary is the oldest at {Mary} years old")
    else:
        print(f"Billy is the oldest at {Billy} years old")

# ifTwo()

# * IF STATEMENT - EXAMPLE 3

def ifThree():
    gender = input('Are you a male or a female? ')
    if gender == 'male':
        manHeight = float(input('You are a man. What is your height in meters? '))
        if manHeight > 1.8:
            print('You are quite a tall man')
        elif manHeight > 1.6:
            print('You are not a very short man')
        else:
            print('You are quite a short man')
    elif gender == 'female':
        womanHeight = float(input('You are a woman. What is your height in meters? '))
        if womanHeight > 1.7:
            print('You are quite a tall woman')
        elif womanHeight > 1.5:
            print('You are not a very short woman')
        else:
            print('You are quite a short woman')
    else:
        print("You have entered a wrong gender")
        ifThree()
    tryAgain = input('Do you want to try again? "y" or "n"')
    if tryAgain == 'y':
        ifThree()
            
ifThree()
            