text=str(input("Enter a string: "))
result=""
for ch in text:
    if ch not in "aeiouAEIOU":
        result=result+ch
print(result)
