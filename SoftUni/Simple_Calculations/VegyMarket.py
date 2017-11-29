price_vegy=float(input())
price_fruit=float(input())
kg_vegy=int(input())
kg_fruit=int(input())

if all([price_fruit > 0.00 , price_fruit <= 1000.00 , price_vegy >= 0.00 , price_vegy <= 1000.00 , kg_fruit >= 0.00 , kg_fruit <= 1000.00 , kg_vegy >= 0.00 , kg_vegy <= 1000.00 ]):
    income_lv= ( price_vegy * kg_vegy ) + ( price_fruit * kg_fruit )
    income_eur= income_lv / 1.94
    print(income_eur)
else:print('Всички числа ще са в интервала от 0.00 до 1000.00')
