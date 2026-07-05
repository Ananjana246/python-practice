num1=float(input("Enter first number: "))
num2=float(input("Enter the second number: "))
op=input("Enter the opeartor(+,-,*,/): ")

if op=="+":
    print("result=",num1+num2)
elif op=="-":
    print("result=",num1-num2)
elif op=="*":
    print("result=",num1*num2)
elif op=="/":
    if num2==0:
        print("Division by zero is not possible")
    else:
        print("result=",num1/num2)
else:
    print("Enter valid operator")

