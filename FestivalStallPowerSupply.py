stalls=[200,600,400]
generators=[350,300,700]

stalls.sort()
generators.sort()

print(stalls)
print(generators)

i=0
j=0
count=0

while i<len(stalls) and j<len(generators):
    if stalls[i]<=generators[j]:
        count=count+1
        i=i+1
        j=j+1
    else:
        j=j+1
print(count)