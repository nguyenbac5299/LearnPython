# lambda param: action(param)
from functools import reduce

li = [1, 2, 3]
print(list(map(lambda item: item * 2, li)))
print(list(filter(lambda item: item % 2, li)))
print(reduce(lambda acc, item: acc + item, li))

# exercise
# square
my_list = [5, 4, 3]

print(list(map(lambda item: item ** 2, my_list)))

# list sorting base on the second item

a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda x: x[1])
print(a)
