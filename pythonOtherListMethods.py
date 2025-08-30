
# * EXAMPLE 1 - Count how many times a specified element appears in the list

list1 = [12, 19, 10, 25, 12, 7, 9, 33, 12, 15, 22, 36, 15, 20, 19]

count = list1.count(12)

print(count)

# * EXAMPLE 2 - Determine the index of a specified element in the list

list2 = ["Banana", "Orange", "Pear", "Guava", "Peach", "Lemon", "Fig"]

index1 = list2.index("Lemon")

print(index1)

# * EXAMPLE 3 - Reverse the order of the list

list3 = ['a', 'b', 'c', 'd', 'e']

list3.reverse()

print(list3)

# * EXAMPLE 4 - Sort a simple list

list4 = [19, 7, 13, 1, 10, 15, 5, 20, 29, 9, 4]

list4.sort()

print(list4)

# * EXAMPLE 5 - Sort a complicated list

def sortFunc(x):
  return x['age']

people = [
  {'name': 'Luke', 'age': 20},
  {'name': 'Paul', 'age': 29},
  {'name': 'John', 'age': 26},
  {'name': 'Mary', 'age': 18},
  {'name': 'Trudy', 'age': 28},
  {'name': 'Louis', 'age': 30}
]

people.sort(key=sortFunc, reverse=True)

print(people)