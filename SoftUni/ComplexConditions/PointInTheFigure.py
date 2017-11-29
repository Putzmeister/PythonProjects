h = int(input())
x = int(input())
y = int(input())

if (0 <= x <= (3*h) and y == 0) or ((0<= x <= h or (2*h) <= x <= (3*h)) and y == h) or ((h <= x <= (2*h)) and y == (4*h)):
    print('border')
elif (0 <= y <= h and (x == 0 or x == (3*h))) or (h <= y <= (4*h) and (x == h or x == (2*h))):
    print('border')
elif (0 < x < (3*h) and 0 < y < h) or (h < x < (2*h) and h < y < (4*h)):
    print('inside')
else:
    print('outside')
