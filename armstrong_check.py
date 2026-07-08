number=int(input("Enter a number: "))
digits=str(number)
power=len(digits)

sum_of_powers=0
for digit in digits:
    sum_of_powers+=int(digit)**power
if sum_of_powers==number:
    print("Armstrong number")
else:
    print("Not an armstrong number")