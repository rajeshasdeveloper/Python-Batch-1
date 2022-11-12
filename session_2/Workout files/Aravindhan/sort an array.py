arr= [0 2 1 2 0]
temp==0
lst=[]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
for i in arr:
    lst.append(i)
    print("k",lst)