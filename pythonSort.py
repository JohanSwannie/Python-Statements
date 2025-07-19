

# * EXAMPLE 1 - SORT NUMBERS ASCENDING

list1 = [13, 19, 10, 19, 4, 28, 33]

list1.sort()

print('list1 sorted = ', list1)

# * EXAMPLE 2 - SORT NUMBERS DESCENDING

list2 = [13, 19, 10, 19, 4, 28, 33]

list2.sort(reverse=True)

print('list2 sorted = ', list2)

# * EXAMPLE 3 - SORT ALPHABETIC ASCENDING

list3 = ["Gert", "Jan", "Koos", "Danie", "Hannes", "Zorro"]

list3.sort()

print('list3 sorted = ', list3)

# * EXAMPLE 4 - SORT ALPHABETIC DESCENDING

list4 = ["Gert", "Jan", "Koos", "Danie", "Hannes", "Zorro"]

list4.sort(reverse=True)

print('list4 sorted = ', list4)

# * EXAMPLE 5 - CREATE A NEW SORT FROM EXISTING LIST AND LEAVE EXISTING LIST UNCHANGED

list5 = ["Gert", "Jan", "Koos", "Danie", "Hannes", "Zorro"]

list6 = sorted(list5)

print('list5 unchanged = ', list5)

print('list6 sorted = ', list6)



