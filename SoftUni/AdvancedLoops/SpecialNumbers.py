num = int(input())

for q in range (1, 10):
    for w in range (1, 10):
        for e in range (1, 10):
            for r in range(1, 10):
                if (num % q == 0) and (num % w == 0) and (num % e == 0) and (num % r == 0):
                    print(str(q) + str(w) + str(e) + str(r), end=' ')

