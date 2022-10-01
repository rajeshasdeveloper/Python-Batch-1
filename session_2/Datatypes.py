# str
#  int, float, complex 
# list, tuple, range
# dict
# set, frozenset
# bool
# bytes, bytearray, memoryview
# None


## bool
# True, False

## Truthify values => 1, ' ', 'a', True, '0'
## Flasify values => 0, '', False, None

# set
# set_var_a = {1,2,3,4,5}
# set_var_b = {5,6,7,8}
# set_var_a.add(10)
# set_var_a.remove(10)
# set_var_a.pop()
# print(set_var_a)
# print(set_var_a.difference(set_var_b)) # A - B
# print(set_var_b.difference(set_var_a)) # B - A
# print(set_var_a.union(set_var_b))
# print(set_var_a.intersection(set_var_b))

## frozenset --> immutable

# fset_1 = frozenset({1, 2, 3, 4, 5})
# fset_2 = frozenset({2, 3, 4, 5, 6})
# print(fset_1.difference(fset_2))  # A - B
# print(fset_2.difference(fset_1))  # B - A
# print(fset_1.union(fset_2))
# print(fset_1.intersection(fset_2))

## dict

# dct = dict()
# # dct = {"name": [1,2,3]}
# dct["name"] = "Python"
# dct["date"] = "2022-08-28"
# dct[3] = [1,2,3,4,5]
# dct1 = dct.copy()
# print(dct1)
# b = dct.fromkeys([2,3,4,5])
# print('Get', dct.get('name'))
# print(dct.items())
# print(dct.keys())
# print(dct.values())
# dct.pop('date')
# print("After pop", dct)
# print("Pop item", dct.popitem())
# print("After the pop item", dct)
# flag = dct.setdefault('class', "Python")
# print(flag, '***', dct)
# flag = dct.setdefault('class', "J2E")
# print(flag, '***', dct)
# dct1.update(dct)
# print(dct1)


## range
# range_variable = tuple(range(1, 11, 3))
# print(range_variable)

## slicing

# a = ["a", "b", "c"]
# b = ("a", "b", "c", "d", "e")
# c = "hello wolrd"

# print(b[::-1])


## tuple

# tpl = ('a', 'b', 'c')
# print(tpl)


## list (Array)

list= [3,4,5,6,78]
list.extend()
print(list_copy)











# print("The lst is", lst)
# lst.append("A")
# print("The append 1 in lst is", lst)
# lst.append("B")
# print("The append 2 in lst is", lst)
# lst1 = lst.copy()
# lst.clear()
# print("The clear looks like", lst)
# print("The copy looks like", lst1)
# print("The count of A is", lst1.count("A"))
# lst1.extend(["C", "D"])
# print("The extend looks like", lst1)
# print("The index of A is", lst1.index("A"))
# lst1.insert(1, "F")
# print("The insert looks like", lst1)
# pop_element = lst1.pop(3)
# print("The poped element is", pop_element)
# print("After pop looks like", lst1)
# lst1.remove("B")
# print("Remove looks like", lst1)
# lst1.reverse()
# print("reverse looks like", lst1)
# lst1.sort()
# print("sort looks like", lst1)
# print("sorted look like", sorted(lst1))


# # Number

# int_num = 5
# num_var = 5.0

# num_var = complex(num_var, 6)

# print("num_var is", num_var)
# print("Type of num_var is", type(num_var))
# print("Imaginary part of num_var is", num_var.imag)
# print("Real of num_var is", num_var.real)
# print("The conjugate of num_var is", num_var.conjugate())


# # string

# sample_string = "hello world"

# print("\n\nThis is a memory location of sample_string", id(sample_string))
# print("\n\nThis is a memory location of sample_string again", id(sample_string))
# print("Upper of samplte_string", sample_string.upper())
# print("Lower  of samplte_string", sample_string.lower())
# print("Title  of samplte_string", sample_string.title())
# print("Capitalize  of samplte_string", sample_string.capitalize())
# print("Count of l", sample_string.count("l"))
# print("Endswith", sample_string.endswith("d"))
# print("Startswith", sample_string.startswith("W"))
# print("isAplha", sample_string.isalpha())
# print("isNumeric", sample_string.isnumeric())
# print("is alpha numeric", sample_string.isalnum())
# print("Find of l", sample_string.find("l"))
# print("rfind of l", sample_string.rfind("l"))
# print("Before strip", sample_string)
# print("strip returns", sample_string.strip())
# print("split returns", sample_string.split())
# print("replace returns", sample_string.replace("world", "python"))
# print(
#     "This is a memory location of replaced string",
#     id(sample_string.replace("world", "python")),
# )
