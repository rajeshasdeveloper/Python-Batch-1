arr_1=[1,2,3,5,7,9,12]
missing_no_array=[]
for i in range(arr_1[0],arr_1[-1]+1):
    if i not in arr_1:
        missing_no_array.append(i)
print(missing_no_array)  
