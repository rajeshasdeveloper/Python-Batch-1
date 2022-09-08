a=[1,2,3,4,5,6]
b=[10,4,5,6,7,78]
c=[]
for i in a :
    c.append(i)
for j in b:
    if j not in  c:
        c.append(j)
print("union of a and b is",c)