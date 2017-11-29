num = float(input())
source = input()
destination = input()

convertion = {'m': 1 , 'mm':1000 , 'cm': 100 , 'mi':0.000621371192 , 'in': 39.3700787 , 'km': 0.001 , 'ft': 3.2808399 , 'yd': 1.0936133}

result = (num / convertion[source]) * convertion[destination]

print(str(result) + ' ' + destination)

