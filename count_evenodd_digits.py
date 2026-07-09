number=int(input("Enter a number: "))
even=0
odd=0
while number>0:
    digit=number%10
    if digit%2==0:
        even+=1
    else:
        odd+=1
    number=number//10
print("Even digits:",even)
print("Odd digits",odd)