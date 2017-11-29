bitcoins = int(input())
chinese = float(input())
comission = float(input())

if 0 <= bitcoins <= 20 and 0.00 <= chinese <= 50000.00 and 0.00 <= comission <= 5.00:
    leva = (bitcoins * 1168) + (chinese * 0.15 * 1.76)
    euro = (leva / 1.95) -  (comission / 100 * (leva / 1.95))
    print(euro)

