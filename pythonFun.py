
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



