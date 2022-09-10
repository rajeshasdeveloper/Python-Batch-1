#missing_elements
a = [1,2,3,5]
missing_elements = []
for i in range(a[0], a[-1]+1):
    if i not in a:
        missing_elements.append(i)
print(missing_elements)