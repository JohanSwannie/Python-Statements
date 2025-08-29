sum = 0

while True:
    try:
        repeat = int(input("How many number do you want to add up together? - "))
        break
    except ValueError:
        print("Please enter a valid number")
        
for x in range(1, repeat + 1):
    while True:
        try:
            number = int(input(f"Please enter number {x} - "))
            sum += number
            break
        except ValueError:
            print("Please enter a valid number")

print(f"The final result = {sum}")
        