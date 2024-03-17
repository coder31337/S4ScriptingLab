num = int(input('Enter a number: '))
og_num = num

rev_num = 0
while num > 0:
    last_digit = num % 10
    rev_num = rev_num * 10 + last_digit
    num //= 10

if og_num == rev_num:
    print('Number is a palindrome')
else:
    print('Number is not a palindrome')
