def say_hello():
    print('hello')


say_hello()
print(say_hello)  # print place of memory save say_hello function


# dry stand for do not repeat yourself function


# parameters
def say_hello(name, age):
    print(f' hello {name}: {age}')


# argument
say_hello('Bac', 21)


# default parameter

def say_hello(name='Bac', age='18', first_name='nguyen'):
    print(f'{first_name} {name} : {age}')


say_hello()


def sum(num_1, num_2):
    return num_2 + num_1
    # if not return=> auto return none


total = sum(1, 2)
print(sum(1, total))
print(sum(1, sum(1, 2)))


def sum_1(item1, item2):
    def sum_2(n1, n2):
        return n1 + n2

    return sum_2(item1, item2)


print(sum_1(10, 20))


# Docstring
def test(a):
    '''
    infor: this function test and print param a
    :param a:
    :return:
    '''
    print(a)


test('!!!')
help(test)
test.__doc__


# clean code
def is_even(num):
    return num % 2 == 0


print(is_even(50))
