i = 0
while i < 10:
    print(i)
    i += 1
else:
    print('end')
i = 0
while i < 10:
    print(i)
    i += 1
    break
else:
    print('end')  # not execute because has break

# while True:
#     response = input('Say something: ')
#     if response == 'bye':
#         break

for i in [1, 2, 3]:
    if i == 2:
        continue
    print(i)

# exercise
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
for image in picture:
    for pixel in image:
        if pixel:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

# exercise: Check for duplicates in list
my_list = ['a', 'b', 'c', 'b', 'm', 'n', 'n']
duplicates=[]
for i in my_list:
    if (my_list.count(i)>1) and (i not in duplicates):
        duplicates.append(i)
print(duplicates)
