j=[12,34,45,23,111]
a=j[0]
b=j[0]
for i in j:
    if i>a:
        a=i
    if i<b:
         b=i
print("The maximum number is",a)
print("The minimum number is",b)

