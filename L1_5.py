

a = int(input('Введите выручку - '))
b = int(input('Введите издержки - '))
prib = a - b
if prib > 0:
    print('ваша компания прибыльна')
    print('Рентабельность составляет', prib/a)
    q = int(input('Сколько сотрудников у вас работает - '))
    print('Прибыль на одого сотрудника составляет ', prib / q)
else:
    print('ваша компания убыточна')





