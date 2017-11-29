town = input().lower()
sales = float(input())

if sales > 0 and ( town == 'sofia' or town == 'plovdiv' or town == 'varna'):
    if town == 'sofia':
        if 0 <= sales <= 500:
            comission = 0.05
            print('%.2f' % (comission * sales))
        elif 500 < sales <= 1000:
            comission = 0.07
            print('%.2f' % (comission * sales))
        elif 1000 < sales <= 10000:
            comission = 0.08
            print('%.2f' % (comission * sales))
        elif sales > 10000:
            comission = 0.12
            print('%.2f' % (comission * sales))
    elif town == 'varna':
        if 0 <= sales <= 500:
            comission = 0.045
            print('%.2f' % (comission * sales))
        elif 500 < sales <= 1000:
            comission = 0.075
            print('%.2f' % (comission * sales))
        elif 1000 < sales <= 10000:
            comission = 0.10
            print('%.2f' % (comission * sales))
        elif sales > 10000:
            comission = 0.13
            print('%.2f' % (comission * sales))
    elif town == 'plovdiv':
        if 0 <= sales <= 500:
            comission = 0.055
            print('%.2f' % (comission * sales))
        elif 500 < sales <= 1000:
            comission = 0.08
            print('%.2f' % (comission * sales))
        elif 1000 < sales <= 10000:
            comission = 0.12
            print('%.2f' % (comission * sales))
        elif sales > 10000:
            comission = 0.145
            print('%.2f' % (comission * sales))

if sales < 0 or (town != 'sofia' or town != 'plovdiv' or town != 'varna'):
    print('error')


