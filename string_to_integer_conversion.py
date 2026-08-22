values = ["10", "20", "abc", "40"]

for item in values:
    try:
        number = int(item)
        print(number)
    except ValueError:
        print("invalid number")
        