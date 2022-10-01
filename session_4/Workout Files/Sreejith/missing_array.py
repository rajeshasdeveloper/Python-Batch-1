arr_1 =[1,2,3,4,5,6,7,10]
missing_numbers=[]
for i in range(arr_1[0],arr_1[-1]+1):
    if i not in arr_1:
        missing_numbers.append(i)
print(missing_numbers)
