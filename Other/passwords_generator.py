import random

n = int(input('Enter password length: '))

def password_generator(lenght):

    alphabet = (
                'abcdefghijklmnopqrstuvwxyz' 
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                '0123456789'
                '!@#$%^&*()_-+.,'
                )

    password = ''
    for i in range(lenght):
        char = random.choice(alphabet)
        password += char
    return password


print(password_generator(n))
