# class BigObject:
#     pass
#
#
# object1 = BigObject()
# print(type(object1))

class PlayerCharacter:
    # static available
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name
            self.age = age

    def run(self, string):
        print(f'{string}')
        return 'done'

    def shout(self):
        print(f'my name is {self.name}')

    # class method: run without even instantiate
    # can use to instantiate a cls
    @classmethod
    def adding_things(cls, num1, num2):
        # return num1 + num2
        return  cls('Bac',num1* num2)

    # static method
    # same class method but not need cls
    @staticmethod
    def adding_things2(num1, num2):
        return num2*num1


player1 = PlayerCharacter('Bac', 21)
player2 = PlayerCharacter('Hai', 22)
player1.attack = 50

player3= PlayerCharacter.adding_things(2,3)
print(player3.age)

print(player1.name)
print(player1.run('Hello'))
print(player1.attack)
print(player1.membership)
print(PlayerCharacter.membership)
print(player1.shout())
print(player2.age)
