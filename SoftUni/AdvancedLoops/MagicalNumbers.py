num = int(input())

for q in range (1, 10):
    for w in range (1, 10):
        for e in range (1, 10):
            for r in range(1, 10):
                for t in range(1, 10):
                    for y in range(1, 10):
                        if q * w * e * r * t * y == num:
                            print(str(q) + str(w) + str(e) + str(r) + str(t) + str(y), end=' ')