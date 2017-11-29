hours = int(input())
minutes = int(input())


totalminutes = hours * 60 + minutes

resultminutes = totalminutes + 15

displayhours = resultminutes // 60
displayminutes = resultminutes % 60



if displayminutes < 10 and displayhours < 24:
    print(str(displayhours) + ':0' + str(displayminutes))
elif displayminutes < 10 and displayhours >= 24:
    bighours = displayhours - 24
    print(str(bighours) + ':0' + str(displayminutes))
elif displayminutes >= 10 and displayhours >= 24:
    bighours = displayhours - 24
    print(str(bighours) + ':' + str(displayminutes))
else:
    print(str(displayhours) + ':' + str(displayminutes))



