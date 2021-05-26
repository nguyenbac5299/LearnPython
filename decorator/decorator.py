# Hight Order Function HOC
# a function accepts inside of its parameter
def greet(func):
    func()


def greet2():
    def func():
        return 5

    return func


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('********')
        func()
        print('*********')

    return wrap_func

@my_decorator
def hello():
    print('hello')


def helloo():
    print('hellooooooo')

def hellooo(name, emoji=':)'):
    print(f'hello {name} {emoji}' )


hello()
my_decorator(helloo)()
hellooo('Bac')


from time import time
def performance(func):
    def wrapper(*args, **kwargs):
        t1=time()
        result=func(*args, **kwargs)
        t2=time()
        print(f'{t2-t1}')
        return result
    return wrapper
@performance
def long_time():
    for i in range(10):
        i*5

long_time()

#exercise
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:

user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)