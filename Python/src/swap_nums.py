x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

print('\nNumbers before swapping')
print('X =', x, '\t', 'Y =', y)

x, y = y, x

print('\nNumbers after swapping')
print('X =', x, '\t', 'Y =', y)
