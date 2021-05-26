# 1- start with local
# 2- parent local?
# 3- global
# 4- built in python function

# global keyword
total = 0


def count():
    global total
    total+= 1
    return total

def count(total):
    total+= 1
    return total

print(count(count(count(total))))

# nonlocal

def outer():
    x='local'
    def inner():
        nonlocal x
        x ='nonlocal'
        print('inner: ',x)

    inner()
    print('outer: ',x)
outer()