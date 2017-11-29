n = int(input())
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

if 1 <= n <= 100:
    for i in range(1,n+1):
        currentNum = int(input())
        if 1 <= currentNum < 200:
            num1 += 1
        if 200 <= currentNum < 400:
            num2 += 1
        if 400 <= currentNum < 600:
            num3 += 1
        if 600 <= currentNum < 800:
            num4 += 1
        if 800 <= currentNum <= 1000:
            num5 += 1

p1 = float((num1 / n)*100)
p2 = float((num2 / n)*100)
p3 = float((num3 / n)*100)
p4 = float((num4 / n)*100)
p5 = float((num5 / n)*100)

print(str('%.2f' % p1) + '%')
print(str('%.2f' % p2) + '%')
print(str('%.2f' % p3) + '%')
print(str('%.2f' % p4) + '%')
print(str('%.2f' % p5) + '%')
