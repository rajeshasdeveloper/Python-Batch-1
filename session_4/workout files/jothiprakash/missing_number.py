def missing_number(a):
    for i in range(a[0],a[-1]+1):
        missing_digit=[]
        if i not in a:
            missing_digit.append(i)
            return missing_digit
lst=[1,2,3,4,5,7,8,9]
prabakaran=missing_number(lst)
print(prabakaran)