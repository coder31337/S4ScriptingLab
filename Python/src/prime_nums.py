def is_prime(n):
    if n > 1:
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                return False
        return True
    return False


limit = int(input('Enter a limit: '))
print('Prime numbers upto', limit, 'are', end=' ')
for i in range(limit + 1):
    if is_prime(i):
        print(i, end=' ')
print()
