class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.mydict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return print('Yess??')

    def __getitem__(self, item):
        return self.mydict[item]


action_figure = Toy('red', 0)

print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])


class SupperList(list):
    def __len__(self):
        return 1000


