num = int(input('Enter a number: '))

num_sum = 0
while num > 0:
    last_digit = num % 10
    num_sum += last_digit
    num //= 10

print('Sum of digits is', num_sum)
