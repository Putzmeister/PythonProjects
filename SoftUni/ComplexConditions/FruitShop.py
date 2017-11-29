fruit = input().lower()
day = input()
quantity = float(input())

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        price = 2.5 * quantity
        print('%.2f' % price)
    elif fruit == 'apple':
        price = 1.2 * quantity
        print('%.2f' % price)
    elif fruit == 'orange':
        price = 0.85 * quantity
        print('%.2f' % price)
    elif fruit == 'grapefruit':
        price = 1.45 * quantity
        print('%.2f' % price)
    elif fruit == 'kiwi':
        price = 2.70 * quantity
        print('%.2f' % price)
    elif fruit == 'pineapple':
        price = 5.50 * quantity
        print('%.2f' % price)
    elif fruit == 'grapes':
        price = 3.85 * quantity
        print('%.2f' % price)
    else:
        print('error')
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = 2.70 * quantity
        print('%.2f' % price)
    elif fruit == 'apple':
        price = 1.25 * quantity
        print('%.2f' % price)
    elif fruit == 'orange':
        price = 0.90 * quantity
        print('%.2f' % price)
    elif fruit == 'grapefruit':
        price = 1.60 * quantity
        print('%.2f' % price)
    elif fruit == 'kiwi':
        price = 3.30 * quantity
        print('%.2f' % price)
    elif fruit == 'pineapple':
        price = 5.60 * quantity
        print('%.2f' % price)
    elif fruit == 'grapes':
        price = 4.20 * quantity
        print('%.2f' % price)
    else:
        print('error')




