
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
    list2.pop(index)
print(list2)