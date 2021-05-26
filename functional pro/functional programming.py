from functools import reduce

li = [1, 2, 3]

print('pure function')


def multiply(li):
    new_list = []
    for i in li:
        new_list.append(i * 2)
    return new_list


print(multiply(li))

# map, filter,zip,reduce
# map: iterate over and want to change
print('map')


def multiply1(i):
    return i * 2


print(list(map(multiply1, li)))
print(li)


# filter:iterate and filter base on function( return boolean)

def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, li)))

# zip: zip each item in very object together
your_list = (10, 100, 100)
their_list = [20, 30, 40]

print(list(zip(li, your_list, their_list)))


# reduce
# from functools import reduce
def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, li, 0))
print(reduce(accumulator, li, 10))

# exercise
# from functools import reduce

# 1 Capitalize all of the pet names and print the list

my_pets = ['sisi', 'bibi', 'titi', 'carla']


def cap(item):
    return item.capitalize()


print('---------exercise----------')
print(list(map(cap, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
# sorted(my_numbers)
print(tuple(zip(my_strings,sorted( my_numbers))))
# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def pass_50(item):
    return item > 50

print(list(filter(pass_50, scores)))
# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def total(acc, item):
    return acc+item

print(reduce(total,my_numbers+scores))