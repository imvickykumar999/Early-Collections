import math as m

print('\n...this is vicky.py user defined library, created by Vicky Kumar ;)')

class calci:

    def add(a = 5, b = 2):
        print('Sum of {} and {} is {}'.format(a, b, a+b), end = '\n\n')

    def div(a = 12, b = 5):
        print('a = {}, b = {}'.format(a, b))
        return a/b, a%b

def pie():
    return m.pi

class hello:

    def hi(default_name = 'Vicky'):
        return default_name
        
    def bye(name = 'Ankit'):
        print('Bye, ' + name)