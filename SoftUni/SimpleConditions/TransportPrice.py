kilometer = int(input())
traveltime = str(input())

if 1 <= kilometer < 20 and traveltime == 'day':
    taxi = 0.70 + (0.79 * kilometer)
    print('%.2f' % taxi)
elif 1 <= kilometer < 20 and traveltime == 'night':
    taxi = 0.70 + (0.9 * kilometer)
    print('%.2f' % taxi)
elif 20 <= kilometer < 100 and traveltime == 'day':
    taxi = 0.70 + (0.79 * kilometer)
    bus = 0.09 * kilometer
    if taxi < bus:
        print('%.2f' % taxi)
    else:
        print(bus)
elif 20 <= kilometer < 100 and traveltime == 'night':
    taxi = 0.70 + (0.9 * kilometer)
    bus = 0.09 * kilometer
    if taxi < bus:
        print('%.2f' % taxi)
    else:
        print(bus)
elif 100 <= kilometer <= 5000 and traveltime == 'day':
    taxi = 0.70 + (0.79 * kilometer)
    bus = 0.09 * kilometer
    train = 0.06 * kilometer
    if taxi < bus < train:
        print('%.2f' % taxi)
    elif bus < taxi < train:
        print('%.2f' % bus)
    else:
        print('%.2f' % train)
elif 100 <= kilometer <= 5000 and traveltime == 'night':
    taxi = 0.70 + (0.9 * kilometer)
    bus = 0.09 * kilometer
    train = 0.06 * kilometer
    if taxi < bus < train:
        print('%.2f' % taxi)
    elif bus < taxi < train:
        print('%.2f' % bus)
    else:
        print('%.2f' % train)
