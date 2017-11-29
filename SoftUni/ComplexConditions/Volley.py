import math

yearType = input().lower()
holidays = int(input())
travelWeekends = int(input())

playHolidays = (2 / 3) * holidays
weekendsInSofia = ( 3 / 4 ) * (48 - travelWeekends)
playOtherTown = travelWeekends
play = playHolidays + weekendsInSofia + playOtherTown

if yearType == 'normal':
    play = math.floor(play)
    print(play)
elif yearType == 'leap':
    play = math.floor(play * 1.15)
    print(play)