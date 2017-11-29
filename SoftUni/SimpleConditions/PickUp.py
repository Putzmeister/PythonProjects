import math

loze = int(input())
grozde = float(input())
liters = int(input())
workers = int(input())

if 10 <= loze <= 5000 and 0.00 < grozde <= 10.00 and 10 <= liters <= 600 and 1 <= workers <= 20:
    landForLoze = 0.4 * loze
    wine = (grozde * landForLoze) / 2.5
    if wine < liters:
        shortage = math.floor(liters - wine)
        print('It will be a tough winter! More ' + str(shortage) + ' liters wine needed.')
    else:
        more = math.ceil(wine - liters)
        perWorker = math.ceil(more / workers)
        print('Good harvest this year! Total wine: ' + str(math.floor(wine)) + ' liters.')
        print(str(more) + ' liters left -> ' + str(perWorker) + ' liters per person.')

