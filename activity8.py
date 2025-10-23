my_tuple = ("mouse", [1, 2, 3], (8, 9, 7))
print(my_tuple)
my_tuple = ('p', 'e', 'r', 'm', 't', 'i')
print(my_tuple[0])
print(my_tuple[4])
n_tuple = ("mouse", [1, 2, 3], (8, 9, 7))
print(n_tuple[0][3])
print(n_tuple[1][1])
print("Sliced: ", my_tuple[1:4])
for letter in my_tuple:
    print("Hello", letter)

my_set = {1, 2, 2, 3, 4, 4, 4}
print("Set: ", my_set)
my_set.add(5)
print("Updated set:", my_set)
set1 = my_set
set2 = {2, 4, 4, 6}
print("/n Set 1", set1)
print("Set 2: ", set2)
print("Difference")
print(set1.difference(set2))
print("Symmetric Difference")
print(set1.symmetric_difference(set2))

set3 = {"Green", "Blue"}
set4 = {"Blue", "Yellow"}
print("Original Sets:")
print(set3)
print(set4)
set5 = set3.union(set4)
print("/nUnion of above sets: ")
print(set5)

set6 = {"Red ", "Orange"}
set7 = {"Orange", "Pink"}
print("Original Sets: ")
print(set6)
print(set7)
print("/nIntersection of two said sets: ")
set8 = set6.intersection(set7)
print(set8)