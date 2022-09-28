# Liste

fruit_list = ['apple','pear','grapes']

# Zero-index

print(fruit_list[0]) #primo elemento
print(fruit_list[1]) #secondo element
print(fruit_list[-1]) #ultimo elemento

# Slicing

fruit_list = ['apple','pear','grapes']
print(fruit_list[1:2])
print(fruit_list[:])
print(fruit_list[1:])
print(fruit_list[:1])

# Funzioni

thislist = ["apple", "banana", "cherry"]
print("Initial list", thislist)

thislist.append("strawberry")
print("Updated list:", thislist)
print("Index of 'banana: ", thislist.index("banana"))
print("Get element with negative index", thislist[-2])

new_list = ["mango", "papaya"]
thislist.extend(new_list)
print("Updated list:", thislist)

# Dizionari

prezzi_frutta = {'mela':1.99, 'pera':2.49, 'uva':2.99}
print(prezzi_frutta['mela'])

prezzi_frutta['melone'] = 0.99
prezzi_frutta['fragole'] = 2.29
print(len(prezzi_frutta))

prezzi_frutta.update({"'mela'": "2.19"})

del prezzi_frutta['uva']
print(len(prezzi_frutta))

prezzi_frutta.clear()
print(len(prezzi_frutta))

# Tuple

fruits = ("apple", "banana", "cherry")
print(fruits)
# >>> ('apple', 'banana', 'cherry')
print(len(fruits))
# >>> 3


tuple1 = ("abc", 34, True, 40, "Lorem ipsum")
tuple2 = ("apple", "banana", "cherry")
tuple3 = (1, 3, 13, 99, 3)
tuple4 = (True, False, False)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "pear"
x = tuple(y)

print(x)