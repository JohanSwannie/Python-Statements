
# * FUNCTION - EXAMPLE 1

def printIt():
    print("This is a test to print something")
    
# printIt()

# * FUNCTION - EXAMPLE 2

def whoWorksWhere(list1, list2):
    for i in range(len(list1)):
        print(f"{list1[i]} works for {list2[i]}")
    
list1 = ['Johan', 'Raymond', 'James', 'Alex']
list2 = ['HCLTech', 'Datacom', 'Inland Affairs', 'City Council']

# whoWorksWhere(list1, list2)

# * FUNCTION - EXAMPLE 3

def sumTotals(*args):
    [n1, n2] = args
    sum = n1 + n2
    print(f"The sum of all totals is {sum}")
    
# sumTotals(14, 33)

# * FUNCTION - EXAMPLE 4

def sumTotals(*args):
    sum = args[0] + args[1] + args[2]
    print(f"The sum of all totals is {sum}")
    
# sumTotals(7, 88, 19)

# * FUNCTION - EXAMPLE 5

def sumTotals(**kwargs):
    print(f"His name is {kwargs["firstName"]} {kwargs["lastName"]}")
    
sumTotals(firstName = "Gary", lastName = "Mower"),



