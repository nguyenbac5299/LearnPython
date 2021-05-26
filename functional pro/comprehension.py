# list comprehension
# [ param for param in iterable]

li1 = [char for char in 'hello']
li2 = [num for num in range(10)]
li3 = [num * 2 for num in range(10)]
li4 = [num for num in range(10) if not (num % 2)]
print(li1)
print(li2)
print(li3)
print(li4)

# set comprehension

li1 = {char for char in 'hello'}
li2 = {num for num in range(10)}
li3 = {num * 2 for num in range(10)}
li4 = {num for num in range(10) if not (num % 2)}
print(li1)
print(li2)
print(li3)
print(li4)

# dictionary comprehension
simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
}
new_dict = {k: v ** 2 for k, v in simple_dict.items() if not (v % 2)}
print(new_dict)
new_dict1 = {num: num * 2 for num in [1, 2, 3]}
print(new_dict1)
# exercise

some_list = ['a', 'b', 'c', 'b', 'd', 'n', 'm', 'n']
result_list=list({char for char in some_list})

duplicate=list({char for char in some_list if some_list.count(char)>1})
print(result_list)
print(duplicate)