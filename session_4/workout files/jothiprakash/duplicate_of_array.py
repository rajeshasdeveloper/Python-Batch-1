a=[2,3,4,4,5,5,6,7,7]
count=0
duplicates=[]
for i in range(0,len(a)):
        for j in range(i+1,len(a)):
                if (a[i]==a[j]):
                        duplicates.append(a[j])
print( "The duplicates of given array a is", duplicates)
        
    
    
            


    



    