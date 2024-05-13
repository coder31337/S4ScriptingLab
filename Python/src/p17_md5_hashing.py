import hashlib

string = input('Enter a string to hash: ')
hash = hashlib.md5(string.encode()).hexdigest()
print('MD5 hash is', hash)
