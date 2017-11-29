daysOff = int(input())

if 0<=daysOff<=365:
    workingDays = 365 - daysOff
    playtime = (daysOff * 127) + (workingDays * 63)
    runawaytotal = abs(playtime - 30000)
    runawayhours = int(runawaytotal // 60)
    runawayminutes = (runawaytotal % 60)
    if playtime > 30000:
        print('Tom will run away')
        print(str(runawayhours) + ' hours and ' + str(runawayminutes) + ' minutes more for play')
    else:
        print('Tom sleeps well')
        print(str(runawayhours) + ' hours and ' + str(runawayminutes) + ' minutes less for play')
