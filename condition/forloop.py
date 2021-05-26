for item in 'I\'m Bac':
    print(item)
for i in (1, 2, 3):
    print(i)
for i in {1, 2, 3, 4}:
    for x in ['a', 'b', 'c']:
        print(i, x)

# iterable -list, dictionary, tuple, set, string
# iterated -> one by one check each item in the collection

user = {
    'name': 'Bac',
    'age': 21,
    'is beautiful': True
}
for item in user.items():
    print(item)
for k, v in user.items():
    print(k, v)
for item in user.values():
    print(item)
for item in user.keys():
    print(item)

# counter
sum = 0
list_item = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list_item:
    sum += i
print(sum)

# range

for i in range(0, 10, 2):
    print(i)
for i in range(10):
    print(i)

for i in range(0, 10, -2):
    print(i)  # opposite direction
for _ in range(2):
    print(list(range(10)))
# enumerate
for i, c in enumerate("Hello"):
    print(i, c)
for i, c in enumerate([1, 2, 3]):
    print(i, c)
