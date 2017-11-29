import math

w_meters=float(input())
h_meters=float(input())


if all ([h_meters >= 3 , h_meters <= w_meters , w_meters <= 100]):
    lines=math.floor(( w_meters * 100 ) / 120)
    columns=math.floor(((h_meters - 1)* 100) / 70)
    desks=(columns * lines ) - 3
    print(desks)
else: print('3 ≤ h ≤ w ≤ 100')

