
# # * FOR LOOP - EXAMPLE 1

# def forOne(a, b):
#     for i in range(a, b):
#         print(i)
        
# forOne(3, 8)

# # * FOR LOOP - EXAMPLE 2

# def forTwo(list1):
#     for element in list1:
#         print(element)
#         underline = ''
#         for i in range(len(element)):
#             underline += "-"
#         print(underline)
#         print(" ")
    
# list1 = ["Car", 'Bicycle', "Helicopter", "Bus", "Train", "Plane"]

# forTwo(list1)

# # * FOR LOOP - EXAMPLE 3

# def forThree(cars):
#     for car in cars:
#         if car == 'Nissan':
#             break
#         print(car)
        
# cars = ["BMW", "Mercedes Benz", "Toyota", "Renault", "Volvo", "Nissan", "Ford", "Suzuki"]

# forThree(cars)

# print("-------------------------------------------------------------------------------")

# # * FOR LOOP - EXAMPLE 4

# def forFour(cars2):
#     for car2 in cars2:
#         if car2 == 'Nissan':
#             continue
#         print(car2)
        
# cars2 = ["BMW", "Mercedes Benz", "Toyota", "Renault", "Volvo", "Nissan", "Ford", "Suzuki"]

# forFour(cars2)
            
# # * FOR LOOP - EXAMPLE 5

# def forFive(grp1, grp2):
#     for g1 in grp1:
#         for g2 in grp2:
#             print(g1, g2)
    
    

# group1 = ['Cobol', 'JavaScript', 'Python']
# group2 = ['Programming Language', 'Business Driven', 'Excellent']

# forFive(group1, group2)

# * FOR LOOP - EXAMPLE 6

smallest = float('inf')
list = [2, 5, 12, 9, 74, 1, 15]
for i in list:
    if i < smallest:
        smallest = i
    print('Loop', i, smallest)
print('Smallest', smallest)

# * FOR LOOP - EXAMPLE 7

biggest = float('-inf')

list2 = [14, 6, 19, 3, 28, 10, 5, 11, 18]

for i in list2:
    if i > biggest:
        biggest = i
    print('loop',i, biggest)
print('Biggest', biggest)

