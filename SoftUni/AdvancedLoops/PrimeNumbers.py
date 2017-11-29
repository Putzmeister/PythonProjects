import math
num = int(input())
result = 0
state = True
cycleEND = int(math.sqrt(num))

if num <= 1:
    print('Not Prime')

for i in range (2,num):
    result = num % i
    if result == 0:
        state = False
        break

if state:
    print('Prime')
else:
    print('Not Prime')









