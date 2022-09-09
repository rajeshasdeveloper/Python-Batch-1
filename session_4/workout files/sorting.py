a=[23,45,67,1,3,4]
temp=0
list=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if (a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for i in a:
    list.append(i)
print("sorting of the given array is",list)
