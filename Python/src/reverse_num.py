num = int(input('Enter a number: '))

rev_num = 0
while num > 0:
    last_digit = num % 10
    rev_num = rev_num * 10 + last_digit
    num //= 10

print('The reversed number is', rev_num)
