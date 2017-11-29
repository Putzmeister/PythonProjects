product = input()
day = input()
quantity = float(input())

if day == 'Saturday' or day == 'Sunday':
    if product == 'banana':
        price = 2.7 * quantity
    elif product == 'apple':
        price = 1.25 * quantity
    else:
        print('error')
elif day == 'Monday':
    if product == 'banana':
        price = 2.5 * quantity
    else:
        print('error')
