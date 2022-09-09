a=[51,52,53,55,56,57,58,59]
missing_number=[]
for i in range(a[0],a[-1]+1):
    if i not in a:
        missing_number.append(i)
print(missing_number)