
# * Add Items toa Python List

# * EXAMPLE 1

list1 = [15, 39, 47]

list1.append(33)

print(list1)

# * EXAMPLE 2

list1.insert(3, 12)

print(list1)

# * EXAMPLE 3

list2 = [25, 7, 10]

list1.extend(list2)

print(list1)

# * EXAMPLE 4

list3 = [40, 11, 17]

list1 = list1 + list3

print(list1)

# * EXAMPLE 5 - Copy the list

list4 = ['Potatoes', 'Tomatoes', 'Lettuce']

list5 = list4.copy()

print(isinstance(list5, list))
print(list5)