items = [1, 2, 3, 4, 5, 6]

for i in range(1):
    try:
        index = int(input("Enter an index: "))
        print("Value:", items[index])
    except IndexError:
        print("Error: Index is out of range.")
        