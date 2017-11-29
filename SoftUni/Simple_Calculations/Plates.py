import math

n_ploshtadka = float(input())
w_plochka = float(input())
l_plochka = float(input())
m_peika = float(input())
o_peika = float(input())

area_ploshtadka = n_ploshtadka * n_ploshtadka

area_plochka = w_plochka * l_plochka

area_peika = m_peika * o_peika

if 1 <= n_ploshtadka <= 100 and 0.1 <= w_plochka <= 10.00 and 0.1 <= l_plochka <= 10.00 and 0 <= m_peika <= 10 and 0 <= o_peika <= 10:
    working_area = area_ploshtadka - area_peika
    plochki = (working_area / area_plochka)
    time = (plochki * 0.2)
    print('%.2f' % plochki)
    print('%.2f' % time)

