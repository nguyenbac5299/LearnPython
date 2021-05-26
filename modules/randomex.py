from random import random, choice, randint,shuffle

# help(random) => show all documentation
# dir(random) => show all method
my_list=[1,2,3,4]
print(random())
print(randint(1,10))
print(choice(my_list))
shuffle(my_list)
print(my_list)

# exercises
result= randint(1,10)

while True:
    try:
        guess=int(input(' please enter guess number from 1 to 10: '))
        if 1<= guess <=10 and guess==result:
            print('you are genius!!!')
            break
    except ValueError:
        print('not a number!')
        continue




