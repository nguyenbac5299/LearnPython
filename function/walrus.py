# :=
str = 'hellooooooooooo'
if (n := len(str)) > 14:
    print(f'so long {n}')

while (n := len(str)) > 1:
    print(n)
    str= str[:-1]
    print(str)
