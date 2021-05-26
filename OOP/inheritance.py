class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def attack(self):
        User.attack(self)
        print(f'attacking with arrow of {self.arrow}')

    def run(self):
        print('run very fast!')


wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
archer = Archer('Archer', 50)
# check Inhertiance
# isinstance(instain, Class)
print(isinstance(wizard1, User))


# introspection: the ability to determine the type of an object at runtime


def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer)


# Multile Inheritance
class HybriBorg(Wizard, Archer):
    pass
