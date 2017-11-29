n = int(input())

num1 = 0
num2 = 0
num3 = 0

if 1 <= n <= 1000:
    for i in range(1, n+1):
        currentNum = int(input())
        if currentNum % 2 == 0:
            num1 += 1
        if currentNum % 3 == 0:
            num2 += 1
        if currentNum % 4 == 0:
            num3 += 1

p1 = ( num1 / n )*100
p2 = ( num2/ n )*100
p3 = ( num3 / n )*100

print(('%.2f' % p1) + '%')
print(('%.2f' % p2) + '%')
print(('%.2f' % p3) + '%')





