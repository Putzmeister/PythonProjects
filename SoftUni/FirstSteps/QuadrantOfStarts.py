num = int(input())

print('*' * num)

for i in range(1, (num-1)):
    print('*', end='')
    print(' ' * (num-2), end='')
    print('*')

print('*' * num)