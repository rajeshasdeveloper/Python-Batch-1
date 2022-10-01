num=[20,25,30,35,40,45,50,55,60]
num1=[1,2,3,20,30,50,60,7,8,9]
c=num
for i in num1:
    if i not in c:
        c.append(i)
print("union of num and num1 is", c)        