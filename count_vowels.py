# text=str(input("Enter a string: ")).lower()
# count=0
# for ch in text:
#     if ch in ["a","e","i","o","u"]: 
#         count=count+1
# print(count)

def vowels(text):
    vowels="aeiouAEIOU"
    count=0
    for ch in text:
        if ch in vowels:
            count=count+1
    return(count)
  
text=str(input("Enter a string: "))
print(vowels(text))

