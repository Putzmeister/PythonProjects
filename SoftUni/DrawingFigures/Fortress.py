n = int(input())
lowerDashes = (2*n)-(2*(n//2)+4)
lastLineDots = int(((2*n) - 2 - lowerDashes)/2)

#the top of the fortress
print('/', end='')
print('^' * (n//2), end='')
print(chr(92),end='')
if n > 4:
    print('_' * lowerDashes, end='')
print('/', end='')
print('^' * (n // 2), end='')
print(chr(92))

#body of fortress
for i in range(0, n-3):
    print('|', end='')
    print(' '* (2*n-2), end='')
    print('|')

#bottom of fortress
if n > 4:
    print('|', end='')
    print(' ' * lastLineDots, end='')
    print('_' * lowerDashes, end='')
    print(' ' * lastLineDots, end='')
    print('|')
    print(chr(92),end='')
    print('_' * (n//2), end='')
    print('/',end='')
    print(' ' * lowerDashes, end='')
    print(chr(92), end='')
    print('_' * (n // 2), end='')
    print('/', end='')

else:
    print('|', end='')
    print(' ' * ((2*n) - 2), end='')
    print('|')
    print(chr(92), end='')
    print('_' * (n // 2), end='')
    print('/', end='')
    print(chr(92), end='')
    print('_' * (n // 2), end='')
    print('/', end='')






