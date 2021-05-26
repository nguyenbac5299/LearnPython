my_set = {1, 2, 3, 4, 5, 5}
print(my_set)  # {1,2,3,4,5}
my_set.add(100)
my_set.add(2)

my_list = [1, 2, 3, 4, 5, 5]
my_set = set(my_list)
print(my_set)
print(1 in my_set)
print(len(my_set))
new_set = my_set.copy()
my_set.clear()
print(new_set)

# some method
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set))
print(my_set)
print(your_set.difference(my_set))

my_set.discard(5)
print(my_set)
my_set.difference_update(your_set)
print(my_set)  # {1,2,3} because 4 is removed

my_set.add(4)
my_set.add(5)
print(my_set.intersection(your_set))
# imagine
# my_set & your_set

print(my_set.isdisjoint(your_set))

my_set={1,2,3}
print(my_set.isdisjoint(your_set))

new_set=my_set.union(your_set)
#imagine
# new_set=my_set | your_set

print(my_set.issubset(new_set))
print(new_set.issuperset(my_set))


