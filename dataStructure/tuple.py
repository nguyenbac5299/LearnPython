# Tuple like list but it is immutable
my_tuple = (1, 2, 3, 4, 5, 5, 6)
print(my_tuple[2])
print(3 in my_tuple)
# can't sort, reverse

user = {
    (1, 2, 3): [1, 2, 3],
    'greet': 'hello',
    'age': 21
}
print(user[(1, 2, 3)])
new_tuple = my_tuple[1:4]
x, y, z, *other = (1, 2, 3, 4, 5)
print(new_tuple)
print(x)
print(my_tuple.count(5))
print(my_tuple.index(5, 1, 6))


