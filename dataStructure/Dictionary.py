# Dictionary
dictionary = {
    'a': 1,
    'b': 2
}
print(dictionary['b'])

dictionary = {
    'a': [1, 2, 3],
    'b': 'abc',
    'c': True
}

new_list = [{
    'a': [1, 2, 3],
    'b': 'abc',
    'c': True
},
    {
        'a': [6, 7, 8],
        'b': 'abc',
        'c': True
    }
]
print(new_list[0]['a'][1])

# key: immutable(can not change)

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 21
}
# print(user['age']) # error
print(user.get('age'))  # None
print(user.get('age', 20))  # if age not exits => print default value 20
print(user)

# not common create
user2 = dict(name='Bac', age=22)
print(user2)

# some dictionary method
print('age' in user)
print('age' in user.keys())
print(21 in user.values())
print(user.items())

user1=user.copy()
user.clear()
print(user)
print(user1)

print(user1.pop('age'))
print(user1.popitem())

user1.update({'age':22,'greet':'hello'})
print(user1)






