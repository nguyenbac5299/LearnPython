first_condition = True
second_condition = True
if first_condition and second_condition:
    print(' True and true')
    print('demo multiple statement')
elif first_condition:
    print('First true')
elif second_condition:
    print('Second true')
else:
    print('False and false')

username = 'bac'
password = ''
if username and password:
    print('exist')
else:
    print('not exist')

# ternary operator

# condition_if_true if condition else condition_if_else

is_friend = True
can_massage = 'massage allowed' if is_friend else 'not allowed to massage'
print(can_massage)

# short circuiting
#
# >
# <
# ==
# >=
# <=
# !=
# and
# or
# not

print(1 < 2 < 3 > 4)
print(not (True))
print(not (1 != 1))

# is vs ==
print(' ==')
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])


print('is ')
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print(10 is 10)
print([] is [])
