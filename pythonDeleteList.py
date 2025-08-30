
# * Remove items while iterating through lists

# * EXAMPLE 1

list1 = [13, 18, 19, 10, 22, 3, 17, 29, 35, 23, 40, 31, 37]

for x in list1[:]:
        if x < 20:
            list1.remove(x)

print(list1)

# * EXAMPLE 2

new_list = [x for x in list1 if x > 19]

print(new_list)

# * EXAMPLE 3

list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

indices_to_remove = [1, 2, 3, 4, 5, 10]

for index in sorted(indices_to_remove, reverse=True):
    del list2[index]
#    or list2.pop(index)
print(list2)

# * EXAMPLE 4 - Remove the 1st element

list3 = ['a', True, 'Yes', 9.45, False, 'Mary', 80]

list3.pop(0);

print(list3)

list4 = ['No', 18, False, None, 14.45, 'Yes']

del list4[0]

print(list4)

list5 = [15, 1, 10, 54, 19, 34]

list5 = list5[1:]

print(list5)

# * EXAMPLE 5 - Remove the last element

list6 = ['a', True, 'Yes', 9.45, False, 'Mary', 80]

list6.pop(-1);

print(list6)

list7 = ['No', 18, False, None, 14.45, 'Yes']

del list7[-1]

print(list7)

list8 = [12, 10, 19, 2, 9, 11]

list8 = list8[:-1]

print(list8)

# * EXAMPLE 6 - Delete the complete list

list9 = [18, 55, 7, 10, 29, 13, 30, 18, 27, 44]

list9.clear()

print(f"List 9 is now empty - {list9}")