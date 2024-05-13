import getpass
import math

password = getpass.getpass('Enter password: ')

charset = 0
if any(char.islower() for char in password):
    charset += 26
if any(char.isupper() for char in password):
    charset += 26
if any(char.isdigit() for char in password):
    charset += 10
symbols = '!@#$%^&*-+?'
if any(char in symbols for char in password):
    charset += len(symbols)

print('Password strength is', end=' ')
if charset > 26:
    score = math.log2(charset) * len(password)
    if score > 100:
        print('excellent')
    elif score > 60:
        print('good')
    else:
        print('bad')
else:
    print('bad')
