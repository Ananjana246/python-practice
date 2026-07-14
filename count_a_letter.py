text=str(input("Enter a string: "))
letter=input("Enter a letteer: ")
count=0
for ch in text:
    if ch==letter:
        count=count+1
print(count)
    