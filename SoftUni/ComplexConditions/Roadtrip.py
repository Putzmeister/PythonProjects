budget = float(input())
sesason = input()

if 10.00 <= budget <= 100.00:
    if sesason == 'summer':
        spend = 0.30 * budget
        print('Somewhere in Bulgaria')
        print('Camp - ' + str('%.2f' % spend))
    elif sesason == 'winter':
        spend = 0.70 * budget
        print('Somewhere in Bulgaria')
        print('Hotel - ' + str('%.2f' % spend))
elif 100.00 < budget <= 1000.00:
    if sesason == 'summer':
        spend = 0.40 * budget
        print('Somewhere in Balkans')
        print('Camp - ' + str('%.2f' % spend))
    elif sesason == 'winter':
        spend = 0.80 * budget
        print('Somewhere in Balkans')
        print('Hotel - ' + str('%.2f' % spend))
elif 1000.00 < budget <= 5000.00:
    spend = 0.90 * budget
    print('Somewhere in Europe')
    print('Hotel - ' + str('%.2f' % spend))
