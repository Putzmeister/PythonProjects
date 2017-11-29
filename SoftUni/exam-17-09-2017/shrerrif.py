import math
n = int(input())
dots = math.floor(n/2)+1
xs = n-1


print('.' * int((3*n -1)/2), end='')
print('x', end='')
print('.' * int((3*n -1)/2))

print('.' * int((3*n -3)/2), end='')
print('/x\\', end='')
print('.' * int((3*n -3)/2))

print('.' * int((3*n -3)/2), end='')
print('x|x', end='')
print('.' * int((3*n -3)/2))

for i in range(0,int((n+1)/2)):
    dots -= 1
    xs += 1
    print('.'*dots, end='')
    print('x' * xs, end='')
    print('|', end='')
    print('x' * xs, end='')
    print('.' * dots)


for m in range(0, int(n-((n+1)/2))):
    dots += 1
    xs -= 1
    print('.' * dots, end='')
    print('x' * xs, end='')
    print('|', end='')
    print('x' * xs, end='')
    print('.' * dots)


print('.' * int((3*n -3)/2), end='')
print('/x\\', end='')
print('.' * int((3*n -3)/2))

print('.' * int((3*n -3)/2), end='')
print('\\x/', end='')
print('.' * int((3*n -3)/2))

dots = math.floor(n/2)+1
xs = n-1

for q in range(0,int((n+1)/2)):
    dots -= 1
    xs += 1
    print('.'*dots, end='')
    print('x' * xs, end='')
    print('|', end='')
    print('x' * xs, end='')
    print('.' * dots)


for w in range(0, int(n-((n+1)/2))):
    dots += 1
    xs -= 1
    print('.' * dots, end='')
    print('x' * xs, end='')
    print('|', end='')
    print('x' * xs, end='')
    print('.' * dots)

print('.' * int((3*n -3)/2), end='')
print('x|x', end='')
print('.' * int((3*n -3)/2))

print('.' * int((3*n -3)/2), end='')
print('\\x/', end='')
print('.' * int((3*n -3)/2))

print('.' * int((3*n -1)/2), end='')
print('x', end='')
print('.' * int((3*n -1)/2))