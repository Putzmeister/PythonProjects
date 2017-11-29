n = int(input())

for i in range(1,n-1):
    if i % 2 != 0:
        print('*' * (n-2),end='')
        print(chr(92),end='')
        print(' ',end='')
        print('/',end='')
        print('*' * (n - 2))
    elif i % 2 == 0:
        print('-' * (n - 2), end='')
        print(chr(92), end='')
        print(' ', end='')
        print('/', end='')
        print('-' * (n - 2))

print(' ' * (n-1),end='')
print('@')

for m in range(1,n-1):
    if m % 2 != 0:
        print('*' * (n-2),end='')
        print('/',end='')
        print(' ',end='')
        print(chr(92),end='')
        print('*' * (n - 2))
    elif m % 2 == 0:
        print('-' * (n - 2), end='')
        print('/', end='')
        print(' ', end='')
        print(chr(92), end='')
        print('-' * (n - 2))
