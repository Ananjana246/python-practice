age=int(input("Enter your age: "))
if age<18:
    print("Not eligible")
elif age<=40:
    print("Young voter")
elif age<=60:
    print("Middle-aged voter")
else:
    print("Senior voter")