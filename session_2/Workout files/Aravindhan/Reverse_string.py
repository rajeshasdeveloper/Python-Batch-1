
string = "Aravindhan"

def reverse(string):
    s = " "
    for i in string:
        s = i + s
    return s
print("The original string is:",string)
print("The reverse string is:", reverse(string))

