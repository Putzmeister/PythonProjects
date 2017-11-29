n = int(input())

OddSum = 0
OddMin = 1000000000.0
OddMax = -1000000000.0

EvenSum = 0
EvenMin = 1000000000.0
EvenMax = -1000000000.0

for i in range(1,n+1):
    currentNum = float(input())
    if i % 2 == 0:
        if currentNum > EvenMax:
            EvenMax = currentNum
        if currentNum < EvenMin:
            EvenMin = currentNum
        EvenSum += currentNum
    else:
        if currentNum > OddMax:
            OddMax = currentNum
        if currentNum < OddMin:
            OddMin = currentNum
        OddSum += currentNum

if n == 0:
    print('OddSum=0')
    print('OddMin=No')
    print('OddMax=No')
    print('EvenSum=0')
    print('EvenMin=No')
    print('EvenMax=No')
elif n == 1:
    print('OddSum=%g' % OddSum)
    print('OddMin=%g' % OddMin)
    print('OddMax=%g' % OddMax)
    print('EvenSum=0')
    print('EvenMin=No')
    print('EvenMax=No')
else:
    print('OddSum=%g' % OddSum)
    print('OddMin=%g' % OddMin)
    print('OddMax=%g' % OddMax)
    print('EvenSum=%g' % EvenSum)
    print('EvenMin=%g' % EvenMin)
    print('EvenMax=%g' % EvenMax)



