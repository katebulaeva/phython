

a = int(input('Введите число - '))


b = a%10
print(b)
a = a//10
print(a)

while a > 0:
    if a%10 > b:
        b = a%10
    a = a//10

print('самая большая цифра в вашем числе ', b)