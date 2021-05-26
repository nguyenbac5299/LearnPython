class PlayerCharacter:
    # static available
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            # notation _variable : private
            self._name = name
            self._age = age

    def run(self, string):
        print(f'{string}')
        return 'done'

    def shout(self):
        print(f'my name is {self._name}')
