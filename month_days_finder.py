number=int(input("Enter a month number(1-12): "))
month=[1,3,5,7,8,10,12]
months=[4,6,9,11]
if number in month:
    print("Number of days:31")
elif number in months:
    print("Number of days:30")
elif number==2:
    print("Number of days:28/29")
else:
    print("Enter valid number")