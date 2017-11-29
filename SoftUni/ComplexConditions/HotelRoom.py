month = input().lower()
days = int(input())

if 0 <= days <= 7:
    if month == 'may' or  month == 'october':
        studio = 50 * days
        apartment = 65 * days
        print('Apartment: ' + str('%.2f' % apartment) + ' lv.')
        print('Studio: ' + str('%.2f' % studio) + ' lv.')
    elif month == 'june' or month == 'september':
        studio = 75.20 * days
        apartment = 68.70 * days
        print('Apartment: ' + str('%.2f' % apartment) + ' lv.')
        print('Studio: ' + str('%.2f' % studio) + ' lv.')
    elif month == 'july' or month == 'august':
        studio = 76 * days
        apartment = 77 * days
        print('Apartment: ' + str('%.2f' % apartment) + ' lv.')
        print('Studio: ' + str('%.2f' % studio) + ' lv.')
elif 7 < days <= 14:
    if month == 'may' or  month == 'october':
        studio = (0.95 * 50) * days
        apartment = 65 * days
        print('Apartment: ' + str('%.2f' % apartment) + ' lv.')
        print('Studio: ' + str('%.2f' % studio) + ' lv.')
    elif month == 'june' or month == 'september':
        studio = 75.20 * days
        apartment = 68.70 * days
        print('Apartment: ' + str('%.2f' % apartment) + ' lv.')
        print('Studio: ' + str('%.2f' % studio) + ' lv.')
    elif month == 'july' or month == 'august':
        studio = 76 * days
        apartment = 77 * days
        print('Apartment: ' + str('%.2f' % apartment) + ' lv.')
        print('Studio: ' + str('%.2f' % studio) + ' lv.')
elif days > 14:
    if month == 'may' or  month == 'october':
        studio = (0.70 * 50) * days
        apartment = (0.90 * 65) * days
        print('Apartment: ' + str('%.2f' % apartment) + ' lv.')
        print('Studio: ' + str('%.2f' % studio) + ' lv.')
    elif month == 'june' or month == 'september':
        studio = (0.80 * 75.20) * days
        apartment = (0.90 * 68.70) * days
        print('Apartment: ' + str('%.2f' % apartment) + ' lv.')
        print('Studio: ' + str('%.2f' % studio) + ' lv.')
    elif month == 'july' or month == 'august':
        studio = 76 * days
        apartment = (0.90 * 77) * days
        print('Apartment: ' + str('%.2f' % apartment) + ' lv.')
        print('Studio: ' + str('%.2f' % studio) + ' lv.')
