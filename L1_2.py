sec = int(input('Введите время в секундах -'))

hours = sec // (60*60)

sec = sec - ((sec // (60*60))*(60*60))



min = sec//60

sec = sec - ((sec // 60) * 60)

print("%02i:%02i:%02i" % (hours, min, sec))




