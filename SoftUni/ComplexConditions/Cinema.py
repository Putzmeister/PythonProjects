type = input().lower()
lines = int(input())
columns = int(input())

seat = float(lines * columns)

if type == 'premiere':
    price = 12.00 * seat
    print('%.2f' % price + ' leva')
elif type == 'normal':
    price = 7.50 * seat
    print('%.2f' % price + ' leva')
elif type == 'discount':
    price = 5.00 * seat
    print('%.2f' % price + ' leva')
    