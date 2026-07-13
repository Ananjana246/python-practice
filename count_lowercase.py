text=str(input("Enter a string: "))
count=0
for ch in text:
    if ch.islower():
        count=count+1
print(count)
    