num=int(input("Enter a num: "))
original=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)
if rev==original:
    print("It is palindrome")
else:
    print("No palindrome")