import math

neededhours = int(input())
days = int(input())
overtimeWorkers = int(input())

if 0 <= neededhours <= 200000 and 0 <= days <= 20000 and 0 <= overtimeWorkers <= 200:
    workingDays = 0.9 * days
    workingHours = workingDays * 8
    overtime = overtimeWorkers * 2 * days
    totalhours = math.floor(workingHours + overtime)
    if totalhours >= neededhours:
        lefHours = totalhours - neededhours
        print('Yes!' + str(lefHours) + ' hours left.')
    else:
        lefHours = neededhours - totalhours
        print('Not enough time!' + str(lefHours) + ' hours needed.')

