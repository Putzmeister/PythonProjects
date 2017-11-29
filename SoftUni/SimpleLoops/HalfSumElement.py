import sys

n = int(input())
biggest = -sys.maxsize
SUM = 0

for i in range(1, n+1):
    currentNum = int(input())
    SUM += currentNum
    if currentNum > biggest:
        biggest = currentNum

othersum = SUM - biggest
if othersum == biggest:
    print('Yes')
    print('Sum = ' + str(othersum) )
else:
    print('No')
    print('Diff = ' + str(abs(othersum - biggest)))


