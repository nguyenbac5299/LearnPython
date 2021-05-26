# *args **kwargs
def super_function(*args):
    return sum(args)


print(super_function(1, 2, 3, 4, 5))


def super_function_2(**kwargs):
    total = 0
    for i in kwargs.values():
        total += i
    return total


print(super_function_2(num1=1, num2=2, num3=3))


def super_function_3(*args, **kwargs):
    total = 0
    for i in kwargs.values():
        total += i
    return sum(args) + total


print(super_function_3(1, 2, 3, 4, 5, num1=1, num2=2))

# rule: params, *args, default parameters, **kwargs

# exercises
def highest_even(li):
    even= []
    for i in li:
        if i %2==0:
            even.append(i)
    return max(even)
print(highest_even([1,2,3,4,5,6,7,8]))