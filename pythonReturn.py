
# * RETURN STATEMENT - EXAMPLE 1

def returnOne(name):
    return 'Good Morning ' + name

names = ['Billy', 'Tanya', 'Mary']

for i in range(len(names)):
    print(returnOne(names[i]))
    
# * RETURN STATEMENT - EXAMPLE 2

def returnTwo(list, total):
    for i in range(len(list)):
        total += list[i]
    return total
        

list1 = [53, 18, 199, 234, 77, 37, 184, 16, 200, 20]
total = 0

print(f"The sum of all the totals in the list is {returnTwo(list1, total)}")