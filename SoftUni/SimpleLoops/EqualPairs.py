import sys


n = int(input())

maxsum = -sys.maxsize
maxdiff = -sys.maxsize
sum = dict()



for i in range(1, n+1):
    currentNum1 = float(input())
    currentNum2 = float(input())
    sum[i] = (currentNum1 + currentNum2)
    if sum[i] > maxsum:
       maxsum = float(sum[i])
    if i > 1:
        diff = abs(float(sum[i]) - float(sum[i-1]))
        if diff > maxdiff:
            maxdiff = diff


if n == 1:
    print('Yes, value=%g' % maxsum)
elif diff == 0:
    print('Yes, value=%g' % maxsum)
else:
    print('No, maxdiff=%g' % maxdiff)

