budget = float(input())
category = input().lower()
people = int(input())

if 1000.00 <= budget <= 1000000.00:
    if category == 'vip':
        if 1 <= people <= 4:
            money = 0.25 * budget
            price = people * 499.99
            left = money - price
            if left >= 0:
                print('Yes! You have ' + str('%.2f' % left) + ' leva left.')
            elif left < 0:
                print('Not enough money! You need ' + str('%.2f' % abs(left)) + ' leva.')
        elif 5 <= people <= 9:
            money = 0.4 * budget
            price = people * 499.99
            left = money - price
            if left >= 0:
                print('Yes! You have ' + str('%.2f' % left) + ' leva left.')
            elif left < 0:
                print('Not enough money! You need ' + str('%.2f' % abs(left)) + ' leva.')
        elif 10 <= people <= 24:
            money = 0.5 * budget
            price = people * 499.99
            left = money - price
            if left >= 0:
                print('Yes! You have ' + str('%.2f' % left) + ' leva left.')
            elif left < 0:
                print('Not enough money! You need ' + str('%.2f' % abs(left)) + ' leva.')
        elif 25 <= people <= 49:
            money = 0.6 * budget
            price = people * 499.99
            left = money - price
            if left >= 0:
                print('Yes! You have ' + str('%.2f' % left) + ' leva left.')
            elif left < 0:
                print('Not enough money! You need ' + str('%.2f' % abs(left)) + ' leva.')
        elif people > 50:
            money = 0.75 * budget
            price = people * 499.99
            left = money - price
            if left >= 0:
                print('Yes! You have ' + str('%.2f' % left) + ' leva left.')
            elif left < 0:
                print('Not enough money! You need ' + str('%.2f' % abs(left)) + ' leva.')
    elif category == 'normal':
        if 1 <= people <= 4:
            money = 0.25 * budget
            price = people * 249.99
            left = money - price
            if left >= 0:
                print('Yes! You have ' + str('%.2f' % left) + ' leva left.')
            elif left < 0:
                print('Not enough money! You need ' + str('%.2f' % abs(left)) + ' leva.')
        elif 5 <= people <= 9:
            money = 0.4 * budget
            price = people * 249.99
            left = money - price
            if left >= 0:
                print('Yes! You have ' + str('%.2f' % left) + ' leva left.')
            elif left < 0:
                print('Not enough money! You need ' + str('%.2f' % abs(left)) + ' leva.')
        elif 10 <= people <= 24:
            money = 0.5 * budget
            price = people * 249.99
            left = money - price
            if left >= 0:
                print('Yes! You have ' + str('%.2f' % left) + ' leva left.')
            elif left < 0:
                print('Not enough money! You need ' + str('%.2f' % abs(left)) + ' leva.')
        elif 25 <= people <= 49:
            money = 0.6 * budget
            price = people * 249.99
            left = money - price
            if left >= 0:
                print('Yes! You have ' + str('%.2f' % left) + ' leva left.')
            elif left < 0:
                print('Not enough money! You need ' + str('%.2f' % abs(left)) + ' leva.')
        elif people > 50:
            money = 0.75 * budget
            price = people * 249.99
            left = money - price
            if left >= 0:
                print('Yes! You have ' + str('%.2f' % left) + ' leva left.')
            elif left < 0:
                print('Not enough money! You need ' + str('%.2f' % abs(left)) + ' leva.')
