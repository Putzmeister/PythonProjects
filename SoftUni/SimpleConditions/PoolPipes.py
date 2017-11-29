v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

if 1 <= v <= 10000 and 1 <= p1 <= 5000 and 1 <= p2 <= 5000:
    voda = (p1 * h) + (p2 * h)
    if voda < v:
        xFull = int((voda / v) * 100)
        yPipe1 = int((p1 * h) / voda * 100)
        yPipe2 = int((p2 * h) / voda * 100)
        print('The pool is ' + str(xFull) + '% full. Pipe 1: ' + str(yPipe1) + '%. Pipe 2: ' + str(yPipe2) + '%.' )
    else:
        overflow = (voda - v)
        print('For ' + str(h) + ' hours the pool overflows with ' + str(overflow) + ' liters.')

