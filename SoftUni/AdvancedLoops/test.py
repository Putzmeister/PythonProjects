n = int(input())
l = int(input())
max = 0

for q in range(1, n):
    for m in range(1, n):
        if m >= q:
            max = m
        else:
            max = q
        for i in range(0, l):
            for z in range(0, l):
                for x in range(max+1,n+1):
                    print(q,end='')
                    print(m,end='')
                    print(chr((97 + i)),end='')
                    print(chr((97 + z)), end='')
                    print(str(x) + ' ', end='')


