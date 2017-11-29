age = int(input())
washingMachine = float(input())
toyPrice = int(input())
toys = 0
birthdayMoney = 0
sumBirthdayMoney = 0

if 1 <= age <= 77 and 1.00 <= washingMachine <= 10000.00 and 0 <= toyPrice <= 40:
    for i in range(1, age + 1):
        if i % 2 != 0:
            toys += 1
        if i % 2 == 0:
            birthdayMoney += 10
            sumBirthdayMoney += birthdayMoney - 1

toysMoney = toys * toyPrice
totalMoney = sumBirthdayMoney + toysMoney

if totalMoney >= washingMachine:
    print('Yes! ' + str('%.2f' % (totalMoney - washingMachine)))
else:
    print('No! ' + str('%.2f' % (washingMachine - totalMoney)))
