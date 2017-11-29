number = int(input())
countPass = 0
password ='test'

for q in range(1,10):
    for w in range(1, 10):
        for e in range(1, 10):
            for r in range(1, 10):
                if ((q*w) + (e*r) == number) and ( q < w ) and (e > r):
                    countPass += 1
                    print('%d%d%d%d' % (q,w,e,r), end=' ')
                    if countPass == 4:
                       password = str(q)+str(w)+str(e)+str(r)

if countPass == 0:
    print('No!')
elif countPass < 4:
    print()
    print('No!')
else:
    print()
    print('Password: ' + str(password))
