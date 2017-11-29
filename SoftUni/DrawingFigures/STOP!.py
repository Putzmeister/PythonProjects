n = int(input())

#upper line
lowerDashesTop = int((2 * n) + 1)
spacesTop = int(((4*n + 3) - lowerDashesTop) / 2)

print('.' * spacesTop, end='')
print('_' * lowerDashesTop, end='')
print('.' * spacesTop)

for i in range(0,n):
    print('.' * (n-i), end='')
    print('//', end='')
    print('_' * ((2*n -1) + (2 * i)), end='')
    print(chr(92) * 2, end='')
    print('.' * (n-i))

#middle line
lowerDashesMiddle = int(((4*n + 3)-9)/2)
print('//', end='')
print('_' * lowerDashesMiddle, end='')
print('STOP!', end='')
print('_' * lowerDashesMiddle, end='')
print(chr(92) * 2)

#lower part
for m in range(0,n):
    lowerDashesBottom = int((4 * n - 1) - (2 * m))
    print('.' * m, end='')
    print(chr(92) * 2, end='')
    print('_' * lowerDashesBottom, end='')
    print('//', end='')
    print('.' * m)

