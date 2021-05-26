# interable
# interate
# generator

def generator_function(num):
    for i in range(num):
        yield i*2


g = generator_function(10)
next(g)
print(next(g))
print(next(g))


for i in generator_function(10):
    print(i)


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
    print('1')
    for i in range(10000):
        i*5
@performance
def long_time_2():
    print('2')
    for i in list(range(10000)):
        i*5

long_time()
long_time_2()



def fun_gen(num):
    for i in range(num):
        yield i

for i in fun_gen(10):
    print(i)



def special_for(iterable):
    iterator=iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)

        except StopIteration:
            break

special_for([1,2,3])

# exercises
print('exercises fibonancy:')
def fib(num):
    a=0
    b=1
    for i in range(num):
        yield a
        tem=a
        a=b
        b=tem+b

for i in fib(20):
    print(i)

