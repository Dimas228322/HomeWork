duration = int(input('Введите число'))
minutes = 60
hours = 3600
day = 86400
while duration < minutes:
    print(duration,'сек')
    break
if minutes < duration <= hours:
    min1 = duration // minutes
    min2 = duration % minutes
    print(min1,'мин')
    print(min2,'сек')
elif hours < duration:
    min3 = duration // hours
    min4 = duration % hours
    min5 = min4 // minutes
    min6 = min5 % minutes
    print(min3,'час',min5,'мин',min6,'сек')









