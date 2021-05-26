# Error Handling

while True:
    try:
        age=int(input('Enter your age: '))
        raise Exception('hey! it cut')
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thanks!!!')
        break
    finally:
        print('done one time')

def div(num1, num2):
    try:
        num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'Error: {err}')

div('1',0)
