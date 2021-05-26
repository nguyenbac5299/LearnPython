class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Cat1', 1)
cat2 = Cat('Cat2', 2)
cat3 = Cat('Cat3', 3)


def max_age(*args):
    return max(args)


print(f'max age is : {max_age(cat1.age, cat2.age, cat3.age)}')



