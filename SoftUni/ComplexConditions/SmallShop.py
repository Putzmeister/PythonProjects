product = input().lower()
town = input().lower()
quantity = float(input())

price = 0

if town == 'sofia':
    if product == 'coffee':
        price = 0.5 * quantity
    elif product == 'water':
        price = 0.8 * quantity
    elif product == 'beer':
        price = 1.2 * quantity
    elif product == 'sweets':
        price = 1.45 * quantity
    elif product == 'peanuts':
        price = 1.6 * quantity
elif town == 'plovdiv':
    if product == 'coffee':
        price = 0.4 * quantity
    elif product == 'water':
        price = 0.7 * quantity
    elif product == 'beer':
        price = 1.15 * quantity
    elif product == 'sweets':
        price = 1.30 * quantity
    elif product == 'peanuts':
        price = 1.50 * quantity
elif town == 'varna':
    if product == 'coffee':
        price = 0.45 * quantity
    elif product == 'water':
        price = 0.7 * quantity
    elif product == 'beer':
        price = 1.10 * quantity
    elif product == 'sweets':
        price = 1.35 * quantity
    elif product == 'peanuts':
        price = 1.55 * quantity

print('%.2f' % price)

