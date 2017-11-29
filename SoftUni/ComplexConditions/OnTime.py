hourExam = int(input())
minutesExam = int(input())
hourArrive = int(input())
minutesArrive = int(input())

if 0 <= hourExam <= 23 and 0 <= minutesExam <= 59  and 0 <= hourArrive<= 23 and 0 <= minutesArrive <= 59:
    totalExam = (hourExam * 60) + minutesExam
    totalArrive = (hourArrive * 60) + minutesArrive
    totalDifference = totalArrive - totalExam
    if -60 < totalDifference < -30:
        print('Early')
        print(str(abs(totalDifference)) + " minutes before the start")
    elif -60 >= totalDifference:
        hourEarly = abs(totalDifference) // 60
        minutesEarly = abs(totalDifference) % 60
        if 0 <= minutesEarly < 10:
            print('Early')
            print(str(hourEarly) + ':0' + str(minutesEarly) + ' hours before the start')
        else:
            print('Early')
            print(str(hourEarly) + ':' + str(minutesEarly) + ' hours before the start')
    elif 0 < totalDifference < 60:
        print('Late')
        print(str(abs(totalDifference)) + " minutes after the start")
    elif totalDifference >= 60:
        hourEarly = abs(totalDifference) // 60
        minutesEarly = abs(totalDifference) % 60
        if 0 <= minutesEarly < 10:
            print('Late')
            print(str(hourEarly) + ':0' + str(minutesEarly) + ' hours after the start')
        else:
            print('Late')
            print(str(hourEarly) + ':' + str(minutesEarly) + ' hours after the start')
    elif -30 <= totalDifference < 0:
        print('On time')
        print(str(abs(totalDifference)) + " minutes before the start")
    elif totalDifference == 0:
        print('On time')



