workdays = int(input())
paycheck = float(input())
change = float(input())

if 5 <= workdays <= 30 and 10.00 <= paycheck <= 2000.00 and 0.99 <= change <= 1.99:
    money = workdays * 12 * paycheck * change
    bonus = money / 12 * 2.5
    taxes = (money + bonus) * 0.25
    profit = money + bonus - taxes
    profitPerDay = profit / 365
    print('%.2f' % profitPerDay)
