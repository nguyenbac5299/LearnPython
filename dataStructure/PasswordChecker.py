name = input('User name: ')
password = input('Password: ')
password_len = len(password)
hidden_password = password_len * '*'
print(f'{name}, your password: {hidden_password} is {password_len} letters long')
