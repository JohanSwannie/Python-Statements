
# * Fun Tricks 1 - Create a second list with data types from another list

list = [12, 'Panda', 13, None, 17, True, 'Joe']         

list2 = ["String" if isinstance(x, str) else "Boolean" if isinstance(x, bool) else "Number" if isinstance(x, int) else x for x in list]

print(list2)

# * Fun Tricks 2 - Merge Dictionaries

j = {'Gary': 16, "Mary": 13, "Luke": 21, "Eugene": 19}
k = {"Carl": 22, "Freddy": 24, "Gary": 20, "Hank": 21, "Mary": 23, "Luke": 20}
l = {"Carl": 30, "Gary": 28, "Eugene": 33}

m = {**j, **k, **l}
print(m)

# * Fun Tricks 3 - Iterate with enumerate() instead of range(len())

# * Old Way

numberList = [21, 51, 16, 9, 78, 5]

for i in range(len(numberList)):
    if numberList[i] > 50:
        numberList[i] = "Clear Winner"
        
print(numberList)

# * Better Way

numberList2 = [10, 15, 76, 4, 18, 55]

for index1, number in enumerate(numberList2):
    if number > 50:
        numberList2[index1] = "Clear Winner"

print(numberList2)

# * Fun Tricks 4 - Use list comprehension instead of for loops

# * Old Way

evenNumbers = []
for x in range(1, 11):
    evenNumbers.append(x + x)

print(evenNumbers)

# * Better Way

evenNumbers2 = [x + x for x in range(1, 11)]

print(evenNumbers2)

# * Fun Tricks 5 - Sort complex iterables

personDict = [{"name": "Jacky", "age": 29}, 
              {"name": "Luke", "age": 19}, 
              {"name": "Carlos", "age": 22},
              {"name": "Benjamin", "age": 23}
        ]
personDict_Sorted = sorted(personDict, key=lambda x: x["age"])

print(personDict_Sorted)

# * Fun Tricks 6 - Create sets from lists to eliminate duplicates

list3 = ['Cat', 14, True, "Dog", 28, 14, "Cat", False, 21, True]

set1 = set(list3)

print(set1)

